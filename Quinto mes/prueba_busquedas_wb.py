# cadena = "Hola, bienvenido 217864328 p3874b{""a mi aplicacion en Python"
# cantidad =  cadena.count("b") #Cuántas incidencias hay

# print(cantidad)

# cantidad1 = cadena.find("ni") # En qué posición está la incidencia
# print(cantidad1)

# Expresiones regulares
import re
cadenat =  "En esta cadena se encuentra una palabra magica, y sigo buscando más cosas"

encontrado = re.search("magica", cadenat)

if encontrado:
    print("La palabra si se encuetra en la cadena")
    print(f"Inicia en la posición {encontrado.start()}")
    print(f"Termina en la posición {encontrado.end()}")
else:
    print("La palabra no se encuetra en la cadena")

cadenac = "1 23 hola ariosto es 67 1000 que si se 976 puede &**&"
cadenac_array = re.split(" ", cadenac)

for valor in cadenac_array:
    print(valor)


numero = "67a"
es_numero = numero.isdigit()

if es_numero:
    print("Tu valor es un número")
else:
    print("Tu valor no es un número")

