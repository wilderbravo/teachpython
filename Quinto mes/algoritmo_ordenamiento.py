#Búsqueda Lineal
from random import sample

# lista = [2,3,4,6,7,4,7,8,9,0]
lista = sample(range(0,1000000), 1000000)
elemento = 780

def busqueda_lineal(lista, elemento):
    
    for i in lista:
        if (i==elemento):
            return True
    
    return False

respuesta = busqueda_lineal(lista, elemento)

print(lista)

if (respuesta):
    print("El elemento si se encuentra en la lista")
else:
    print("El elemento no se encuentra en la lista")