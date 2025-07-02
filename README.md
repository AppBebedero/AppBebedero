
# 📢 Sistema de Alertas – Liceo de Bebedero

Este es un sistema web desarrollado por **José Daniel Quesada M.** en **Flask (Python)** para el registro y seguimiento de **alertas tempranas** en el Liceo de Bebedero.

El sistema permite:
- Enviar alertas a la Oficina de Orientación y a la Dirección del Liceo
- Registrar motivos académicos, disciplinarios o personales
- Visualizar reportes filtrados por fecha, sección o estudiante (solo accesibles con autorización, ya que están protegidos por clave)

📬 **Contacto del desarrollador:**  
Correo: [jdaniel.quesadam@gmail.com](mailto:jdaniel.quesadam@gmail.com)  
Celular: 8788-9993

---

## 🚀 Características principales

- 📝 Formulario web intuitivo para envío de alertas  
- 🔄 Conexión a Google Sheets con respaldo automático y envío de correos  
- ✅ Diseño adaptable a celulares, tabletas y computadoras  
- 🔐 Acceso seguro con clave para visualizar reportes  
- 📊 Módulo de reportes con múltiples filtros (fecha, sección, estudiante)  
- ☁️ Implementación en [PythonAnywhere](https://AppBebedero.pythonanywhere.com)

---

## 📁 Estructura del proyecto

```
AppBebedero/
├── mysite/
│   ├── flask_app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── inicio.html
│   │   ├── index.html
│   │   └── reportes.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
├── secciones.csv
├── alumnos.csv
├── acciones.csv
├── dimensiones.csv
└── README.md
```

---

## 🔄 Envío de datos

Los datos del formulario se envían mediante `POST` a un **Google Apps Script** que:

- Registra la alerta en la hoja `Alertas` de Google Sheets
- Genera un ID único y un timestamp
- Envía automáticamente un correo electrónico con los detalles

🔗 **URL del script:**  
https://script.google.com/macros/s/AKfycbwG8YUEG0tZO1P_iP3pGtriHWu453wb_wfULGG0aYRRvq8oHovDfPBIuFdFqBN6VodhwQ/exec

---

## 📊 Módulo de reportes

Los reportes permiten:
- Ver todas las alertas registradas
- Filtrar por:
  - Fecha o rango de fechas
  - Sección o estudiante
  - Semana, mes o año

> ⚠️ Solo usuarios con clave pueden acceder a esta sección.

---

## 🧪 Tecnologías utilizadas

- Python 3 + Flask (framework web)
- HTML5 / CSS3 / JavaScript
- Google Apps Script (integración con Google Sheets)
- PythonAnywhere (hosting en la nube)
- pandas (procesamiento de reportes)
- GitHub (control de versiones)

---

## 👤 Autor

Desarrollado por:  
**José Daniel Quesada M.**  
Correo: jdaniel.quesadam@gmail.com  
Celular: 8788-9993

---

## 📌 Licencia

Proyecto de uso educativo y privado.  
Todos los derechos reservados.  
Liceo de Bebedero – 2025.

