from datetime import date, datetime, timedelta


def _convertir_fecha(texto):
	for formato in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
		try:
			return datetime.strptime(texto, formato).date()
		except ValueError:
			continue
	return None


def leer_horario():
	texto_fecha = input("Fecha (DD/MM/AAAA o AAAA-MM-DD): ").strip()
	dia = _convertir_fecha(texto_fecha)
	if dia is None:
		print("Fecha inválida. Ejemplos: 04/10/2026 o 2026-10-04.")
		return None
	try:
		hora = datetime.strptime(input("Hora (HH:MM): ").strip(), "%H:%M")
		duracion = int(input("Duración en minutos: ").strip())
	except ValueError:
		print("Hora o duración inválida.")
		return None
	if dia < date.today() or not 1 <= duracion <= 480:
		print("Fecha pasada o duración fuera del rango 1-480.")
		return None
	fecha = dia.isoformat()
	inicio = datetime.combine(dia, hora.time())
	if (inicio + timedelta(minutes=duracion)).date() != dia:
		print("La práctica debe terminar el mismo día.")
		return None
	return fecha, hora.strftime("%H:%M"), duracion, inicio


def hay_cruce(citas, fecha, hora, duracion, cliente, instructor, placa):
	inicio = datetime.strptime(fecha + " " + hora, "%Y-%m-%d %H:%M")
	fin = inicio + timedelta(minutes=duracion)
	for cita in citas:
		if cita["fecha"] != fecha:
			continue
		otro = datetime.strptime(cita["fecha"] + " " + cita["hora"], "%Y-%m-%d %H:%M")
		fin_otro = otro + timedelta(minutes=cita["duracion"])
		recursos = (cita["cliente"] == cliente or cita["instructor"] == instructor
					or cita["placa"] == placa)
		if inicio < fin_otro and otro < fin and recursos:
			return True
	return False


def nuevo_codigo(citas):
	codigo = f"CITA-{len(citas) + 1:04d}"
	while any(cita["codigo"] == codigo for cita in citas):
		codigo = f"CITA-{int(codigo[-4:]) + 1:04d}"
	return codigo
