from flask import Flask, render_template, request
import csv
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta'

# Ruta base para archivos locales
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Función genérica para leer CSV
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
            "profesor": request.form.get("profesor")
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

if __name__ == '__main__':
    app.run(debug=True)




