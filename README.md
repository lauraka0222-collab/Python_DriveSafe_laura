# Academia DriveSafe

Sistema de consola para administrar clientes, instructores, vehículos y citas de práctica. Los datos se guardan localmente en archivos JSON.

## Requisitos

- Python 3.10 o posterior.
- No requiere instalar paquetes externos.

## Cómo ejecutar

Desde la carpeta del proyecto, ejecuta:

```bash
python main.py
```

## Menú principal

| Opción | Acción |
| --- | --- |
| 1 | Registrar cliente |
| 2 | Consultar clientes |
| 3 | Registrar instructor |
| 4 | Consultar instructores |
| 5 | Registrar vehículo |
| 6 | Consultar vehículos |
| 7 | Programar cita de práctica |
| 8 | Consultar citas por cliente o fecha |
| 9 | Registrar asistencia y observaciones |
| 10 | Consultar el historial de un cliente |
| 11 | Abrir el menú de examen |
| 0 | Salir |

Los clientes, instructores y vehículos deben registrarse antes de programar una cita. El tipo de vehículo del cliente, la especialidad del instructor y el tipo del vehículo deben coincidir. Tampoco se puede programar con un vehículo no disponible ni asignar a un cliente, instructor o vehículo a dos citas que se crucen en el horario.

## Ejemplo de uso

1. En la opción **1**, registra el documento `CLI001`, el nombre `Ana Demo` y el tipo `moto`.
2. En la opción **3**, registra el documento `INS001`, el nombre `Luis Demo` y la especialidad `moto`.
3. En la opción **5**, registra la placa `DEM123`, el tipo `moto` y marca el vehículo como disponible (`s`).
4. En la opción **7**, ingresa `CLI001`, `INS001` y `DEM123`. Indica una fecha futura (por ejemplo, `31/12/2099`), una hora como `09:00` y una duración en minutos (entre 1 y 480).
5. Después de programar, el sistema solo muestra un mensaje de confirmación; no muestra el código de la cita. Usa la opción **8** sin filtros para encontrarla y copiar su código (por ejemplo, `CITA-0001`).
6. Usa la opción **9**, ingresa ese código y responde `si` o `no`. Después puedes añadir observaciones.
7. Consulta las citas con la opción **8** o el historial de `CLI001` con la opción **10**.

## Formatos aceptados

- Tipos de vehículo y especialidades: `moto` o `carro`.
- Fechas de citas del menú principal: `DD/MM/AAAA`, `DD-MM-AAAA` o `AAAA-MM-DD`.
- Horas: formato de 24 horas, `HH:MM`.
- Duración de una práctica: de 1 a 480 minutos; la práctica debe terminar el mismo día.
- En la opción **8**, los filtros de documento y fecha son opcionales (pulsa Enter para omitirlos). La fecha del filtro debe tener formato `AAAA-MM-DD`.
- Al registrar un vehículo, indica disponibilidad con `s` o `n`.

## Menú de examen

La opción **11** abre un menú separado para consultar las citas del día o registrar una cita básica. Para esta opción, la fecha debe escribirse como `AAAA-MM-DD`. La cita básica solicita cliente, instructor, vehículo, fecha y hora; esos datos se guardan como texto y no se comprueba que correspondan a registros existentes.

**Importante:** el menú de examen y el menú principal guardan las citas en `citas.json`, pero utilizan estructuras de datos incompatibles. Mezclar registros puede causar errores al consultar citas o registrar asistencia. Además, el menú de examen comprueba si el instructor ya tiene una cita a esa hora sin tener en cuenta la fecha. Para gestionar las citas de la academia, usa el menú principal y no mezcles registros creados desde ambos menús.

## Archivos de datos

Los archivos se encuentran junto al código. Si no existen, el sistema inicia con listas vacías; se crean o actualizan al guardar datos.

- `clientes.json`: documento, nombre y tipo de vehículo de cada cliente.
- `instructores.json`: documento, nombre y especialidad de cada instructor.
- `vehiculos.json`: placa, tipo y disponibilidad de cada vehículo.
- `citas.json`: citas programadas, incluida la información de cliente, instructor, vehículo, fecha, hora, duración, asistencia y observaciones.
