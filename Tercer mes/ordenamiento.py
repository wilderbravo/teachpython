numeros = [16, 4, 9, 1, 3, 20, 8, -7, 4, 5, 16]

print(numeros)
numeros.sort()
print(numeros)

palabras = ["hola", "coche", "burro", "avión", "manzana", "perro", "gato"]
print(palabras)
palabras.sort()
print(palabras)

# lista = [1, "a", 5, "g", 3, "c"]
# print(lista)
# lista.sort()
# print(lista)
print("--"*50)
numeros = [16, 4, 9, 1, 3, 20, 8]
ordenados = sorted(numeros)
print(numeros)
print(ordenados)

# Reverse 1
print("=="*50)
numeros = [16, 4, 9, 1, 3, 20, 7, -4, 54, 8]
print(numeros)
numeros.sort(reverse=True)
print(numeros)

# Reverse 2
print("=="*50)
numeros = [16, 4, 9, 1, 3, 20, 7, -4, 54, 8]
print(numeros)
ordenados = sorted(numeros, reverse=True)
print(ordenados)

#Ordenamiento diccionarios
diccionarios_coches = [
        {'color': 'Rojo', 'matricula': '4859-A', 'cambio': 'A'},
        {'color': 'Azul', 'matricula': '2901-Z', 'cambio': 'M'},
        {'color': 'Gris', 'matricula': '1892-B', 'cambio': 'M'}
]
print("=="*50)
print(diccionarios_coches)
ordenados_coches = sorted(diccionarios_coches, key=lambda coche: coche["cambio"])
print(ordenados_coches)

