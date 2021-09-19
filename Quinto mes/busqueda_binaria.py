import random 
from random import sample

def busqueda_binaria(lista, inicio, final, objetivo):
    print(f"Buscando {objetivo} entre {lista[inicio]} y {lista[final-1]}")
    if (inicio > final):
        return False
    
    medio = (inicio + final) // 2 #División de enteros

    if (lista[medio]==objetivo):
        return True
    elif(lista[medio] < objetivo):
        return busqueda_binaria(lista, medio +1, final, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio -1, objetivo)

tamano_lista = int(input("Por favor ingrese el tamaño de la lista: "))
objetivo = int(input("Por favor ingrese el objetivo a buscar: "))

lista = sorted(sample(range(0,1000000), tamano_lista))
encontrado = busqueda_binaria(lista, 0, len(lista)-1, objetivo)
print(encontrado)
print(lista)
print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')