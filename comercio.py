def calcular_cambio(monto_total, monto_entregado):
    cambio = monto_entregado - monto_total
    if cambio < 0:
        print("El monto entregado no es suficiente.")
        return None

    billetes = [500, 100, 50, 20, 10, 5, 1]
    cambio_a_dar = {billete: 0 for billete in billetes}

    for billete in billetes:
        while cambio >= billete:
            cambio_a_dar[billete] += 1
            cambio -= billete

    return cambio_a_dar


monto_total = float(input("Ingrese el monto total de la compra: "))
monto_entregado = float(input("Ingrese el monto entregado por el cliente: "))

cambio = calcular_cambio(monto_total, monto_entregado)
if cambio:
    print("Cambio a dar:")
    for billete, cantidad in cambio.items():#-
        print(f"{billete} billetes: {cantidad}")#+
