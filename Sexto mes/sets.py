# my_set = {3, 4, 5}
# print(f"my_set = {my_set}")

# my_set2 = {"Hola", 2.3, False, True}
# print("my_set2 = ", my_set2)

# my_set3 = {3, 3, 2}
# print("my_set3 = ", my_set3)

# my_set4 = {[1, 2, 3], 4}
# print("my_set4 = ", my_set4)

# Declaración
# empty_set = {} # Diccionario
# print(type(empty_set))

# empty_set = set()
# print(type(empty_set))

# Casting con sets

# my_list = [1, 1, 2, 3, 4, 4, 5]
# my_set = set(my_list)
# print(my_set)

# my_tuple = ("Hola", "Hola", "Hola", 1)
# my_set2 = set(my_tuple)
# print(my_set2)

# Añadir elementos a un set

# my_set = {1, 2, 3}
# print(my_set)
# my_set.add(4)
# print(my_set)

# my_set.update([1, 2, 5, 6])
# print(my_set)

# my_set.update([1, 2, 5], [6, 8])
# print(my_set)

# # Quitar elementos

# my_set = {1, 2, 3, 4, 5, 6, 7}
# print(my_set)

# my_set.discard(1)
# print(my_set)

# my_set.remove(2)
# print(my_set)

# my_set.discard(10)
# print(my_set)

# my_set.remove(12)
# print(my_set)

# # Otro ejemplo de borrado (Borrar elemento aletaroerio)
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

my_set.pop()
print(my_set)

#Limpiar el set
my_set.clear()
print(my_set)
