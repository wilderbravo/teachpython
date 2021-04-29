# Ejercicio para clase de funciones
def mi_funcion():
    print("Hola Amigo")

def suma():
    res = 34 + 2
    print(f"El resultado es {res}")

def suma_return():
    res = 15 + 10

    return res

def suma_parametros(valor1, valor2):
    res = valor1 + valor2

    return res

mi_funcion()#Llamado de función con Hola
suma()#LLamado de función que suma
suma_respuesta = suma_return()
print(f"el resultado devuelto es {suma_respuesta}")

print("--"*50)
suma_resultado = suma_parametros(10,30)
print(f"El resultado Con parametros es {suma_resultado}")