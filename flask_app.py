from flask import Flask, render_template, request, jsonify
import csv
import requests
import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def leer_csv(nombre_archivo):
    ruta = os.path.join(BASE_DIR, nombre_archivo)
    with open(ruta, encoding='utf-8') as f:
        return list(csv.reader(f))[1:]

def obtener_secciones():
    return [fila[0] for fila in leer_csv('Secciones.csv') if fila]

def obtener_alumnos():
    return [{"seccion": fila[0], "alumno": fila[1]} for fila in leer_csv('Alumnos.csv') if len(fila) >= 2]

def obtener_acciones():
    return [fila[0] for fila in leer_csv('Acciones.csv') if fila]

def obtener_dimensiones():
    return [fila[0] for fila in leer_csv('Dimensiones.csv') if fila]

def obtener_motivos():
    return [{"dimension": fila[0], "motivo": fila[1]} for fila in leer_csv('Motivos.csv') if len(fila) >= 2]

def obtener_profesores():
    return [fila[0] for fila in leer_csv('Profesores.csv') if fila]

def enviar_alerta_por_correo(info):
    try:
        remitente = 'alertas.bebedero@gmail.com'
        contraseña = 'xcvajtntwvgixkb'
        destinatarios = ['alejandra.quesada.soto@mep.go.cr', 'josedanny09@gmail.com']
        asunto = '🔐 Intento de acceso no autorizado a Reportes'

        cuerpo = f"""
⚠️ Se detectó un intento fallido de acceso a Reportes

📅 Fecha y hora: {info['hora']}
🌐 IP: {info['ip']}
📍 Ubicación: {info['ubicacion']}
🏢 Proveedor: {info['org']}
📱 Dispositivo/Navegador: {info['user_agent']}
"""

        msg = MIMEText(cuerpo)
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = ', '.join(destinatarios)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente, contraseña)
            servidor.send_message(msg)

    except Exception as e:
        print("❌ Error al enviar correo:", e)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    secciones = obtener_secciones()
    alumnos = obtener_alumnos()
    acciones = obtener_acciones()
    dimensiones = obtener_dimensiones()
    motivos = obtener_motivos()
    profesores = obtener_profesores()
    mensaje = ""

    if request.method == 'POST':
        datos = {
            "seccion": request.form.get("seccion"),
            "alumno": request.form.get("alumno"),
            "accion": request.form.get("accion"),
            "dimension": request.form.get("dimension"),
            "motivo": request.form.get("motivo"),
            "observaciones": request.form.get("observaciones"),
            "consecutivo": request.form.get("consecutivo"),
            "profesor": request.form.get("profesor"),
            "timestamp": request.form.get("timestamp")
        }

        try:
            respuesta = requests.post(
                'https://script.google.com/macros/s/AKfycbwG8YUEG0tZO1P_iP3pGtriHWu453wb_wfULGG0aYRRvq8oHovDfPBIuFdFqBN6VodhwQ/exec',
                json=datos
            )
            if respuesta.status_code == 200 and "OK" in respuesta.text:
                mensaje = "✅ ¡Alerta enviada correctamente!"
            else:
                mensaje = f"⚠️ Error inesperado: {respuesta.text}"
        except Exception as e:
            mensaje = f"❌ Fallo en la conexión: {str(e)}"

    return render_template(
        "index.html",
        secciones=secciones,
        alumnos=alumnos,
        acciones=acciones,
        dimensiones=dimensiones,
        motivos=motivos,
        profesores=profesores,
        mensaje=mensaje
    )

@app.route('/reportes', methods=['GET', 'POST'])
def reportes():
    GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/1SodhlgFh8lyzJ_e6h4UJhNlB9lDzKdIo9kpZ9M-oovY/export?format=csv&gid=476352620"

    try:
        df = pd.read_csv(GOOGLE_SHEET_CSV_URL)

        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d/%m/%Y %H:%M:%S', errors='coerce')

        desde_raw = request.form.get('desde', '').strip()
        hasta_raw = request.form.get('hasta', '').strip()

        if desde_raw and hasta_raw:
            desde = pd.to_datetime(desde_raw, format='%Y-%m-%d', errors='coerce').date()
            hasta = pd.to_datetime(hasta_raw, format='%Y-%m-%d', errors='coerce').date()
            df = df[df['Timestamp'].dt.date.between(desde, hasta)]

        df = df.sort_values(by='Timestamp', ascending=False)
        registros = df.to_dict(orient='records')

    except Exception as e:
        registros = []
        print(f"❌ Error al cargar datos de reportes: {e}")

    return render_template(
        'reportes.html',
        registros=registros,
        desde=request.form.get('desde', ''),
        hasta=request.form.get('hasta', '')
    )

@app.route('/verificar_clave', methods=['POST'])
def verificar_clave():
    clave_ingresada = request.json.get('clave', '')

    try:
        with open(os.path.join(BASE_DIR, 'clave.txt'), 'r', encoding='utf-8') as f:
            clave_correcta = f.read().strip()
    except:
        return jsonify({'resultado': 'error', 'mensaje': 'No se pudo leer la clave del sistema.'})

    if clave_ingresada == clave_correcta:
        return jsonify({'resultado': 'ok'})
    else:
        ip = request.remote_addr
        try:
            respuesta = requests.get(f'https://ipinfo.io/{ip}/json').json()
            ciudad = respuesta.get('city', 'Desconocida')
            region = respuesta.get('region', '')
            pais = respuesta.get('country', '')
            org = respuesta.get('org', 'Desconocido')
            ubicacion = f"{ciudad}, {region}, {pais}".strip(', ')
        except Exception:
            ubicacion = "Desconocida"
            org = "Desconocido"

        info = {
            'ip': ip,
            'ubicacion': ubicacion,
            'org': org,
            'user_agent': request.headers.get('User-Agent', 'Desconocido'),
            'hora': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }

        enviar_alerta_por_correo(info)

        return jsonify({
            'resultado': 'error',
            'mensaje': '🔒 Su clave es incorrecta o usted no está autorizado a ingresar a Reportes'
        })

if __name__ == '__main__':
    app.run(debug=True)
