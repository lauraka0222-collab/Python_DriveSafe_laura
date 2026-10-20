from gestionar_json import guardar_datos
from validaciones import buscar, tipo_valido


def registrar_cliente(datos):
	documento = input("Documento: ").strip()
	if not documento or buscar(datos["clientes"], "documento", documento):
		print("Documento vacío o ya registrado.")
		return
	nombre = input("Nombre completo: ").strip().title()
	tipo = input("Tipo de vehículo (moto/carro): ").strip().lower()
	if not nombre or not tipo_valido(tipo):
		print("Nombre o tipo de vehículo inválido.")
		return
	datos["clientes"].append({
		"documento": documento, "nombre": nombre, "tipo_vehiculo": tipo,
	})
	guardar_datos(datos)
	print("Cliente guardado.")


def consultar_clientes(datos):
	if not datos["clientes"]:
		print("No hay clientes registrados.")
		return
	for cliente in datos["clientes"]:
		print(f"{cliente['documento']} | {cliente['nombre']} | {cliente['tipo_vehiculo']}")
