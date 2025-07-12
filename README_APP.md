# 📦 Rama `app-donada`

Esta rama contiene la versión oficial **donada al colegio** (Liceo de Bebedero) del sistema de Alertas Tempranas.

### ✅ Características:
- Formulario con listas desplegables dependientes.
- Subida de imágenes documentales.
- Envío de correos automáticos a la Oficina de Orientación y Dirección.
- Reportes protegidos con clave (`clave.txt`).
- Página de **cambio de clave** accesible desde el menú Configuración.
- Interfaz adaptable para móviles (PWA).
- Diseño elegante y botones accesibles.

### 🔐 Clave de acceso a reportes
- Guardada en el archivo `clave.txt`.
- Cambiable desde `/configuracion`.

### 🛠 Archivos importantes
- `flask_app.py` — archivo principal de la app.
- `templates/base.html` — base del diseño de la interfaz.
- `templates/cambiar_clave.html` — formulario para cambiar clave.
- `static/uploads/` — carpeta para guardar imágenes.

---

### 🧭 Nota
Esta rama **no debe mezclarse con `colegio-configurable`**, ya que cada una corresponde a una versión distinta de la app.

