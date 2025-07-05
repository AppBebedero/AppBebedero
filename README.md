# 📢 Sistema de Alertas – Liceo de Bebedero

Este es un sistema web desarrollado por **José Daniel Quesada M.** en **Flask (Python)** para el registro y seguimiento de **alertas tempranas** en el Liceo de Bebedero, Cañas, Guanacaste.

El sistema permite:
- Enviar alertas a la Oficina de Orientación y a la Dirección del Liceo
- Registrar motivos académicos, disciplinarios o personales
- Visualizar reportes filtrados por fecha, sección o estudiante (solo accesibles con autorización, ya que están protegidos por clave)

---

## 🚀 Características principales

- 📝 Formulario web intuitivo para envío de alertas
- 🔄 Conexión a Google Sheets con respaldo automático y envío de correos
- ✅ Diseño adaptable a celulares, tabletas y computadoras
- 🔐 Acceso seguro con clave para visualizar reportes
- 📊 Módulo de reportes con múltiples filtros:
  - Por rango de fechas
  - Por sección
  - Por estudiante
  - Combinación de los anteriores
- ☁️ Implementación en [PythonAnywhere](https://AppBebedero.pythonanywhere.com)

---

## 📁 Estructura del proyecto

<pre>
AppBebedero/
├── mysite/
│   ├── flask_app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── inicio.html
│   │   ├── index.html
│   │   ├── reportes.html
│   │   └── manual.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
├── Secciones.csv
├── Alumnos.csv
├── Profesores.csv
├── Acciones.csv
├── Dimensiones.csv
├── Motivos.csv
└── README.md
</pre>

---

## 🔄 Envío de datos

Los datos del formulario se envían mediante `POST` a un **Google Apps Script** que:

- Registra la alerta en la hoja `Alertas` de Google Sheets  
- Genera un ID único y un timestamp  
- Envía automáticamente un correo electrónico con los detalles  

🔗 **URL del script:**  
https://script.google.com/macros/s/AKfycbwG8YUEG0tZO1P3pGtriHWu453wb_wfULGG0aYRRvq8oHovDfPBIuFdFqBN6VodhwQ/exec

---

## 📊 Módulo de reportes

Los reportes permiten:  
- Ver todas las alertas registradas  
- Filtrar por:  
  - Fecha o rango de fechas  
  - Sección (desde el botón **➕ Filtros Avanzados**)  
  - Estudiante (desde el botón **➕ Filtros Avanzados**)  
- Combinar filtros:  
  - Ejemplo: consultar un estudiante específico dentro de una sección en un periodo determinado  

> ⚠️ Solo usuarios con clave pueden acceder a esta sección.

---

## 🧪 Tecnologías utilizadas

- Python 3 + Flask (framework web)  
- HTML5 / CSS3 / JavaScript  
- Google Apps Script (integración con Google Sheets)  
- PythonAnywhere (hosting en la nube)  
- pandas (procesamiento de reportes)  
- GitHub (control de versiones)

---

## 👤 Autor

Desarrollado por:

**José Daniel Quesada M.**  
📧 josedanny09@gmail.com  
📱 8788-9993

---

## 📌 Licencia y Derechos

Este sistema fue desarrollado por **José Daniel Quesada** y donado exclusivamente al **Liceo de Bebedero** para su uso educativo interno.

El autor conserva todos los derechos de propiedad intelectual sobre esta aplicación, incluyendo su diseño, funcionalidad y código fuente.

**No está permitida su reproducción, distribución o modificación por terceros** sin autorización expresa del autor.

La reutilización o adaptación de esta aplicación por parte de otros centros educativos está sujeta a autorización y condiciones establecidas por el autor, incluyendo posibles costos asociados.

© José Daniel Quesada – 2025. Todos los derechos reservados.
