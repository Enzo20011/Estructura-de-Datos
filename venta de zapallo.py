def venta_zapallos():
    precio_base = 1000
    descuentos = {"dolar": 0.05, "yen": 0.15, "guarani": 0.2, "peso": 0.1}

    nombre_comprador = input("Ingrese el nombre del comprador: ")
    nombre_empresa = input("Ingrese el nombre de la empresa: ")
    cantidad = int(input("Ingrese la cantidad de zapallos: "))
    moneda = input("Ingrese la moneda (dolar, yen, guarani, peso, otra): ").lower()

    if moneda in descuentos:
        descuento = descuentos[moneda]
        precio_final = precio_base * (1 - descuento) * cantidad
    else:
        recargo = 0.1
        precio_final = precio_base * (1 + recargo) * cantidad

    print("\n--- Recibo ---")
    print(f"Comprador: {nombre_comprador}")
    print(f"Empresa: {nombre_empresa}")
    print(f"Moneda: {moneda.capitalize()}")
    if moneda in descuentos:
        print(f"Descuento: {descuento * 100}%")
    else:
        print(f"Recargo: {recargo * 100}%")
    print(f"Cantidad: {cantidad} zapallos")
    print(f"Precio total: ${precio_final:.2f} {moneda.upper()}")

venta_zapallos()