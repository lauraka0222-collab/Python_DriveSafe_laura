from fecha import hay_cruce, leer_horario, nuevo_codigo
from gestionar_json import guardar_datos
from validaciones import buscar


def programar_cita(datos):
    cliente = input("Documento del cliente: ").strip()
    instructor = input("Documento del instructor: ").strip()
    placa = input("Placa del vehículo: ").strip().upper()
    persona = buscar(datos["clientes"], "documento", cliente)
    profesor = buscar(datos["instructores"], "documento", instructor)
    vehiculo = buscar(datos["vehiculos"], "placa", placa)
    if not persona or not profesor or not vehiculo:
        print("Verifique que cliente, instructor y vehículo estén registrados.")
        return
    if not vehiculo["disponible"]:
        print("El vehículo no está disponible.")
        return
    if persona["tipo_vehiculo"] != profesor["especialidad"]:
        print("La especialidad del instructor no coincide.")
        return
    if persona["tipo_vehiculo"] != vehiculo["tipo"]:
        print("El vehículo no coincide con el tipo del cliente.")
        return
    horario = leer_horario()
    if horario is None:
        return
    fecha, hora, duracion, inicio = horario
    if hay_cruce(datos["citas"], fecha, hora, duracion, cliente, instructor, placa):
        print("Cliente, instructor o vehículo ya tiene cita en ese horario.")
        return
    datos["citas"].append({
        "codigo": nuevo_codigo(datos["citas"]), "cliente": cliente,
        "instructor": instructor, "placa": placa,
        "tipo_vehiculo": vehiculo["tipo"], "fecha": fecha,
        "hora": hora, "duracion": duracion, "asistencia": None,
        "observaciones": "",
    })
    guardar_datos(datos)
    print("Cita programada correctamente.")