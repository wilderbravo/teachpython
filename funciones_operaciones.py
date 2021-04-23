def suma(parametro1, parametro2):
    res = parametro1 + parametro2

    return res

def resta(parametro1, parametro2):
    res = parametro1 - parametro2

    return res

def multiplica(parametro1, parametro2):
    res = parametro1 * parametro2

    return res

def divide(parametro1, parametro2):
    res = parametro1 / parametro2

    return res

valor1 = int(input("Por favor ingrese un numero entero: \n"))
valor2 = int(input("Por favor ingrese otro numero entero: \n"))
tipo = int(input("Indique el tipo de operacion a realizar: \n"))

if tipo==1:
    respuesta = suma(valor1, valor2)
if tipo==2:
    respuesta = resta(valor1, valor2)
if tipo==3:
    respuesta = multiplica(valor1, valor2)
if tipo==4:
    respuesta = divide(valor1, valor2)

print(f"La respuesta es {respuesta}")

