#Clase de Tuplas
lista_variada = ['perro', 'gato', 'oso', 23, 5.0, True]
for clave, valor in enumerate(lista_variada):
    print (clave, valor)

lista_variada[0]='tigre'
print("--"*50)
print(lista_variada)

# for clave, valor in enumerate(lista_variada):
#     print (clave, valor)

print("--"*50)

lenguajes_programacion = ('Zope', 'Plone', 'Pyramid')
# lenguajes_programacion[0] = 'Carro'# Error, no funciona
print(type(lista_variada))
print(type(lenguajes_programacion))
print("--"*50)
for clave, valor in  enumerate(lenguajes_programacion):
    print (clave, valor)

# for clave, valor in enumerate(lenguajes_programacion):
#     print (clave, valor)
print("--"*50)
print(lenguajes_programacion[0])

# Listas 2 bloques de memoria, tuplas 1 (Eficiencia)


# Cambio de valor para la tupla
# lenguajes_programacion[0] = 'Carro'
