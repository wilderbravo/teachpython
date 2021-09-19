def dividir(valor1, valor2):
    try:
        return True, (valor1 / valor2)
    except:
        return False, 0

def ingreso_float():
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))


# res = dividir(8,0)
# print(res)
# if (res[0]):
#     print(f"La respuesta es {res[1]}")
# else:
#     print("Error en la ejecucuión de la operación")

ingreso_float()