def mayor_estricto(a, b, c):
    max_val = max(a, b, c)
    
    count = (a == max_val) + (b == max_val) + (c == max_val)
    
    if count == 1:
        return max_val
    else:
        return -1


if __name__ == "__main__":
    
    a = int(input("Ingresa el primer número positivo: "))
    b = int(input("Ingresa el segundo número positivo: "))
    c = int(input("Ingresa el tercer número positivo: "))
    
    resultado = mayor_estricto(a, b, c)
    
    if resultado != -1:
        print(f"El mayor valor estricto es: {resultado}")
    else:
        print("No existe un mayor estricto.")
