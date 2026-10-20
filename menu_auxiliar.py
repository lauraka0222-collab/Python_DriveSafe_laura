from datetime import datetime

from gestionar_json import guardar_datos


def _mostrar(datos, cita):
	cliente = next((x for x in datos["clientes"] if x["documento"] == cita["cliente"]), None)
	profesor = next((x for x in datos["instructores"] if x["documento"] == cita["instructor"]), None)
	vehiculo = next((x for x in datos["vehiculos"] if x["placa"] == cita["placa"]), None)
	nombre = cliente["nombre"] if cliente else cita["cliente"]
	nombre_profesor = profesor["nombre"] if profesor else cita["instructor"]
	tipo = cita.get("tipo_vehiculo", vehiculo["tipo"] if vehiculo else "No registrado")
	asistencia = cita["asistencia"]
	estado = "Pendiente" if asistencia is None else ("Sí" if asistencia else "No")
	print(f"{cita['codigo']} | Cliente: {nombre} | Instructor: {nombre_profesor} | "
		  f"Vehículo: {cita['placa']} ({tipo}) | {cita['fecha']} {cita['hora']} | "
		  f"{cita['duracion']} min | Asistió: {estado} | {cita['observaciones']}")


def consultar_citas(datos):
	documento = input("Documento cliente (Enter omite): ").strip()
	fecha = input("Fecha AAAA-MM-DD (Enter omite): ").strip()
	if fecha:
		try:
			datetime.strptime(fecha, "%Y-%m-%d")
		except ValueError:
			print("Fecha inválida.")
			return
	citas = [x for x in datos["citas"]
			 if (not documento or x["cliente"] == documento)
			 and (not fecha or x["fecha"] == fecha)]
	if not citas:
		print("No hay citas con esos filtros.")
	for cita in citas:
		_mostrar(datos, cita)


def registrar_asistencia(datos):
	codigo = input("Código de cita: ").strip().upper()
	cita = next((x for x in datos["citas"] if x["codigo"] == codigo), None)
	if cita is None:
		print("Cita no encontrada.")
		return
	respuesta = input("¿Asistió? (si/no): ").strip().lower()
	if respuesta not in ("si", "no"):
		print("Responda si o no.")
		return
	cita["asistencia"] = respuesta == "si"
	cita["observaciones"] = input("Observaciones: ").strip()
	guardar_datos(datos)
	print("Asistencia guardada.")


def historial_cliente(datos):
	documento = input("Documento del cliente: ").strip()
	citas = [x for x in datos["citas"] if x["cliente"] == documento]
	if not citas:
		print("No hay prácticas para ese cliente.")
	for cita in citas:
		_mostrar(datos, cita)
