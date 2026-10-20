from citas import programar_cita
from clientes import consultar_clientes, registrar_cliente
from gestionar_json import cargar_datos
from instructores import consultar_instructores, registrar_instructor
from menu_auxiliar import consultar_citas, historial_cliente, registrar_asistencia
from vehiculos import consultar_vehiculos, registrar_vehiculo
from menu_examen import menu_examen

def menu_principal():
    datos = cargar_datos()

    while True:
        print("\n=== ACADEMIA DRIVESAFE ===")
        print("1. Registrar cliente")
        print("2. Consultar clientes")
        print("3. Registrar instructor")
        print("4. Consultar instructores")
        print("5. Registrar vehículo")
        print("6. Consultar vehículos")
        print("7. Programar cita de práctica")
        print("8. Consultar citas por cliente o fecha")
        print("9. Registrar asistencia y observaciones")
        print("10. Consultar historial de cliente")
        print("11. menu examen")
        print("0. Salir")

    
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                registrar_cliente(datos)
            case "2":
                consultar_clientes(datos)
            case "3":
                registrar_instructor(datos)
            case "4":
                consultar_instructores(datos)
            case "5":
                registrar_vehiculo(datos)
            case "6":
                consultar_vehiculos(datos)
            case "7":
                programar_cita(datos)
            case "8":
                consultar_citas(datos)
            case "9":
                registrar_asistencia(datos)
            case "10":
                historial_cliente(datos)
            case "11":
                menu_examen()
            case "0":
                print("Gracias por usar el sistema DriveSafe.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")