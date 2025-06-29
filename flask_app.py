from flask import Flask, render_template, request
import csv
import requests
from io import StringIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta'

# 🔹 Lectura de datos desde Google Sheets como CSV
def obtener_datos_desde_csv(gid):
    base_url = "https://docs.google.com/spreadsheets/d/1SodhlgFh8lyzJ_e6h4UJhNlB9lDzKdIo9kpZ9M-oovY/export?format=csv&gid="
    url = base_url + gid
    respuesta = requests.get(url)
    contenido = respuesta.content.decode('utf-8')
    lector = csv.reader(StringIO(contenido))
    return list(lector)

def obtener_secciones():
    datos = obtener_datos_desde_csv("1893025995")
    return [fila[0] for fila in datos[1:] if fila]

def obtener_alumnos():
    datos = obtener_datos_desde_csv("70807267")
    return [{"seccion": fila[0], "alumno": fila[1]} for fila in datos[1:] if len(fila) >= 2]

def obtener_acciones():
    datos = obtener_datos_desde_csv("450918087")
    return [fila[0] for fila in datos[1:] if fila]

def obtener_dimensiones():
    datos = obtener_datos_desde_csv("571366206")
    return [fila[0] for fila in datos[1:] if fila]

def obtener_motivos():
    datos = obtener_datos_desde_csv("1668159635")
    return [{"dimension": fila[0], "motivo": fila[1]} for fila in datos[1:] if len(fila) >= 2]

def obtener_profesores():
    datos = obtener_datos_desde_csv("2098899162")
    return [fila[0] for fila in datos[1:] if fila]

# 🔸 Ruta principal
@app.route('/', methods=['GET', 'POST'])
def home():
    secciones = obtener_secciones()
    alumnos = obtener_alumnos()
    acciones = obtener_acciones()
    dimensiones = obtener_dimensiones()
    motivos = obtener_motivos()
    profesores = obtener_profesores()
    mensaje = ""

    # Depuración en consola para verificar que todo carga bien
    print("✅ Secciones:", secciones[:3])
    print("✅ Alumnos:", alumnos[:3])
    print("✅ Acciones:", acciones[:3])
    print("✅ Dimensiones:", dimensiones[:3])
    print("✅ Motivos:", motivos[:3])
    print("✅ Profesores:", profesores[:3])

    if request.method == 'POST':
        datos = {
            "timestamp": request.form.get("timestamp"),
            "seccion": request.form.get("seccion"),
            "alumno": request.form.get("alumno"),
            "accion": request.form.get("accion"),
            "dimension": request.form.get("dimension"),
            "motivo": request.form.get("motivo"),
            "fecha": request.form.get("fecha"),
            "observaciones": request.form.get("observaciones"),
            "consecutivo": request.form.get("consecutivo"),
            "profesor": request.form.get("profesor"),
        }

        print("✅ Alerta recibida:", datos)
        mensaje = "✅ ¡Alerta enviada correctamente!"

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
