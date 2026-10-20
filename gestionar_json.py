import json
from pathlib import Path


RUTAS = {nombre: Path(__file__).with_name(nombre + ".json")
		 for nombre in ("clientes", "instructores", "vehiculos", "citas")}


def cargar_datos():
	datos = {}
	for nombre, ruta in RUTAS.items():
		try:
			texto = ruta.read_text(encoding="utf-8").strip()
			contenido = json.loads(texto) if texto else []
			datos[nombre] = contenido if isinstance(contenido, list) else []
		except (OSError, json.JSONDecodeError):
			datos[nombre] = []
	return datos


def guardar_datos(datos):
	for nombre, ruta in RUTAS.items():
		with ruta.open("w", encoding="utf-8") as archivo:
			json.dump(datos[nombre], archivo, ensure_ascii=False, indent=4)
