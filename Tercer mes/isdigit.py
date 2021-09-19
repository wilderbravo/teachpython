cadena = str(input("Ingrese un número: "))
if (cadena.isdigit()):
    print(f"Correcto, ingresaste un número {int(cadena)*2}")
else:
    print("Esto no es un número")