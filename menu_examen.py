#Proyecto DriveSafe - Modificación para prueba de Git
import json
from datetime import date, datetime
from pathlib import Path

ARCHIVO = Path(__file__).with_name("citas.json")


def cargar():
    if not ARCHIVO.exists():
        return []
    return json.loads(ARCHIVO.read_text(encoding="utf-8"))


def guardar(citas):
    ARCHIVO.write_text(json.dumps(citas, indent=4), encoding="utf-8")


def pedir(mensaje):
    while not (valor := input(mensaje).strip()):
        print("Error: el valor no puede estar vacío.")
    return valor


def fecha():
    while True:
        try:
            return datetime.strptime(input("Fecha (YYYY-MM-DD): "), "%Y-%m-%d").date()
        except ValueError:
            print("Error: fecha inválida.")


def hora():
    while True:
        try:
            valor = input("Hora (HH:MM): ")
            datetime.strptime(valor, "%H:%M")
            return valor
        except ValueError:
            print("Error: hora inválida.")


def menu_examen():
    while True:
        print("\n=== MENÚ EXAMEN ===")
        print("1. Consultar citas del día")
        print("2. Registrar nueva cita")
        print("3. Volver al menú principal")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            hoy = date.today()
            citas = [c for c in cargar() if date.fromisoformat(c["fecha"]) == hoy]
            print(f"\nCitas del {hoy:%d/%m/%Y}")
            print("\n".join(
                f"{i}. {c['cliente']} - {c['instructor']} - "
                f"{c['vehiculo']} - {c['fecha']} a las {c['hora']}"
                for i, c in enumerate(citas, 1)
            ) or "No existen citas.")
        elif opcion == "2":
            citas = cargar()
            cliente = pedir("Cliente: ")
            instructor = pedir("Instructor: ")
            vehiculo = pedir("Vehículo: ")
            fecha_cita, hora_cita = fecha(), hora()

            if any(
                c["instructor"].lower() == instructor.lower()
                and c["hora"] == hora_cita
                for c in citas
            ):
                print("Error: ya existe una cita con ese instructor y hora.")
                continue

            citas.append({
                "cliente": cliente,
                "instructor": instructor,
                "vehiculo": vehiculo,
                "fecha": fecha_cita.isoformat(),
                "hora": hora_cita,
            })
            guardar(citas)
            print("Cita registrada correctamente.")
        elif opcion == "3":
            return
        else:
            print("Error: opción inválida.")


if __name__ == "__main__":
    menu_examen()