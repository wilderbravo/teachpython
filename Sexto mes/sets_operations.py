"""
    Enlace con información
    https://j2logo.com/python/tutorial/tipo-set-python/
    https://www.programiz.com/python-programming/set
"""

# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}
# my_set21 = {6, 7}

# # Unión de conjuntos
# my_set3 = my_set1 | my_set2
# print(my_set3)

# # Intersección de conjuntos
# my_set3 = my_set1 & my_set2
# print(my_set3)

# # Diferencia de conjuntos
# my_set3 = my_set1 - my_set2
# print(my_set3)
# my_set3 = my_set2 - my_set1
# print(my_set3)

# # Diferencia simétria (Lo contrario a la intersección)
# my_set3 = my_set1 ^ my_set2
# print(my_set3)

# Inclusión de conjuntos 
# En Python se utiliza el operador <= para comprobar si un conjunto A es subconjunto de B y el operador >= 
# para comprobar si un conjunto A es superconjunto de B.
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}
my_set21 = {6, 7}

# my_set3 = my_set1 <= my_set2
# print(my_set3)
# my_set3 = my_set1 >= my_set2
# print(my_set3)
# my_set3 = my_set21 <= my_set2
# print(my_set3)

# Conjuntos disjuntos
# Dos conjuntos A y B son disjuntos si no tienen elementos en común, es decir, la intersección de A y B es el conjunto vacío.
# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a.isdisjoint(b))

# # Igualdad de conjuntos
# a = {1, 2, 3, 4}
# b = {1, 2, 3, 4}
# print(a == b)


import random 

aleatorios = [random.randint(0,50) for _ in range(50)] 
print("Lista con números aleatorios repetidos\n")
print(aleatorios)
print("\n")
aleatorios_sin_repetidos = list(set(aleatorios))
print("Lista con números aleatorios ordenados y quitando repetidos \n")
print(aleatorios_sin_repetidos)