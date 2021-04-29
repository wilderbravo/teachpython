# Convertir números enteros a binarios

# 28

# 28 / 2 = 14 con residuo 0
# 14 / 2 = 7 con residuo 0
# 7 / 2 = 3 con residuo 1
# 3 / 2 = 1 con residuo 1

# 11100

def binario(numero_entero):
    cadena = ''
    numero = numero_entero

    while numero>2:
        cociente = int(numero / 2)
        residuo = numero % 2
        # print(f"Cociente = {cociente} -- Residuo = {residuo}")
        numero = cociente
        cadena = cadena + str(residuo)
    
    cadena = cadena + str(cociente)

    return cadena

def cadena_reves(cadena):
    return cadena[::-1]

print(f"El numero 28 en binario es {cadena_reves(binario(28))}")

# Reto 
# Pedir el numero entero al usuario y que lo convierta en binario
# Hacer las validaciones respectivas