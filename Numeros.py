import datetime

def es_fecha_valida(dia, mes, año):
    try:
        datetime.date(dia,mes,año)
        return True
    except ValueError:
        return False


def programa_verificacion_fecha():
    print("Verificación de fechas:")
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))

    if es_fecha_valida(dia, mes, año):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} no es válida.")


programa_verificacion_fecha()
