from gestionar_json import guardar_datos
from validaciones import buscar, tipo_valido


def registrar_instructor(datos):
	documento = input("Documento del instructor: ").strip()
	if not documento or buscar(datos["instructores"], "documento", documento):
		print("Documento vacío o ya registrado.")
		return
	nombre = input("Nombre completo: ").strip().title()
	especialidad = input("Especialidad (moto/carro): ").strip().lower()
	if not nombre or not tipo_valido(especialidad):
		print("Nombre o especialidad inválidos.")
		return
	datos["instructores"].append({
		"documento": documento, "nombre": nombre, "especialidad": especialidad,
	})
	guardar_datos(datos)
	print("Instructor guardado.")


def consultar_instructores(datos):
	if not datos["instructores"]:
		print("No hay instructores registrados.")
		return
	for instructor in datos["instructores"]:
		print(f"{instructor['documento']} | {instructor['nombre']} | {instructor['especialidad']}")
