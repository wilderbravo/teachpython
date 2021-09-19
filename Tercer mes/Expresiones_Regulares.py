import re
res = re.match("python[^0-9a-z]", "ython+")

print(res)

texto = "ipsum Lorem dolor sit amet, consectetur adipiscing elit"
patron = "Lorem"
x = re.search(patron, texto) #Busca el patron dentro del texto
print(x.span())