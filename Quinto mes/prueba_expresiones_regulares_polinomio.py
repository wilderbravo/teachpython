"""
Mediante expresiones regulares, validar una expresión aritmética como una cadena, 
la misma que después debe ser resuelta, la expresión es la siguiente: a+b^c*(a/c). 
El usuario debe ingresar la expresión con números, por ejemplo 4+5^3*(4/3). 
Si cumple la expresión debe devolver el resultado de dicha operación.
"""
import re

def buscar(cadena):
    evaluar = re.compile(r"^[0-9]{1,3} \+ [0-9]{1,3} \^ [0-9]{1,3} \* \([0-9]{1,3} / [0-9]{1,3}\)$")
    return evaluar.search(cadena)

def resuelve_polinomio(polinomio):
    pass

cadena =  input(str("Señor usuario, por favor ingrese el polinomio de la forma a + b ^ c * (a/c): "))
# cadena = "4 + 5 ^ 3 * (10 / 2)"
# cadena = "4 + 5 ^ 3 * 5"
# cadena = "4 + 125 * 5"
# cadena = "4 + 625"
# cadena = "629"
# patron = ['^[0-9]{1,3} \+ [0-9]{1,3} \^ [0-9]{1,3} \* \([0-9]{1,3} / [0-9]{1,3}\)$']

if buscar(cadena): # Comprobemos que esta es una URL valida
    print("Expresión evaluada correctamente \n")
    resuelve_polinomio(cadena)

else:
    print("Expresión no cumple con la evaluación correcta")
