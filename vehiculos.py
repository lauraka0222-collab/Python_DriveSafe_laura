from gestionar_json import guardar_datos
from validaciones import buscar, tipo_valido


def registrar_vehiculo(datos):
	placa = input("Placa: ").strip().upper()
	if not placa or buscar(datos["vehiculos"], "placa", placa):
		print("Placa vacía o ya registrada.")
		return
	tipo = input("Tipo (moto/carro): ").strip().lower()
	disponible = input("¿Disponible? (s/n): ").strip().lower()
	if not tipo_valido(tipo) or disponible not in ("s", "n"):
		print("Tipo o disponibilidad inválidos.")
		return
	datos["vehiculos"].append({
		"placa": placa, "tipo": tipo, "disponible": disponible == "s",
	})
	guardar_datos(datos)
	print("Vehículo guardado.")


def consultar_vehiculos(datos):
	if not datos["vehiculos"]:
		print("No hay vehículos registrados.")
		return
	for vehiculo in datos["vehiculos"]:
		estado = "Disponible" if vehiculo["disponible"] else "No disponible"
		print(f"{vehiculo['placa']} | {vehiculo['tipo']} | {estado}")
