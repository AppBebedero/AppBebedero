import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_config = os.path.join(BASE_DIR, 'config.json')

try:
    with open(ruta_config, 'r', encoding='utf-8') as archivo:
        config = json.load(archivo)
except Exception as e:
    print(f"❌ Error al cargar config.json: {e}")
    config = {}
