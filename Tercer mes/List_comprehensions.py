count_list = [1,2,3,"a",5,6,7,8,"b",10]
# print(count_list[-2])
# print(count_list[-10], count_list[0])
# print(count_list[:5])# Inicias en 0 hasta la posición 5
# print(count_list[3:])# Desde la posición 3 hasta el finaal
# print(count_list[3:-2])# Desde la posición 3 hasta -2 posiciones desde el final

# lista_cuadrados = [x**2 for x in range(1,100)]
# print(lista_cuadrados)

# lista2 = [2*x for x in range(1,10)]
# print(lista2)

# lista3 = [i for i in range(1, 101) if i % 2 == 0]
# print(lista3)
# points = [(x, y) for y in range(0, 5 + 1) for x in range(0, 10 + 1)]
# print(points)

# lista_iterable = [(x,y) for x in range(1, 10) for y in range(1, 10)]
# print(lista_iterable)

numeros_primos = [x for x in range(2, 50) if all(x % y != 0 for y in range(2, x))]
# print(numeros_primos)

numeros = range(100)

# print(type(numeros))
# Initializar lista de kilómetros
kilometer = [3.2, 3.5, 3.3, 3.8]
# Construcción de  `feet` con `map()`
# feet = map(lambda x: float(3.8399)*x, kilometer) # Reemplazar el valor de kilometer en una nueva lista
# print(feet)
feet1 = [float(3.8399)*x for x in kilometer] # Otra forma de hacer lo mismo con list_comprehnsions
# print(feet1)
# uneven = [x/2 for x in lista1 if x%2==0]
# print(list(feet))
# print(feet1)
# print(uneven)


divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
# print(divided)
# divided1 = [x+1 if x >= 12 else x+5 for x in feet]
# print(divided1)

# list_of_list = [1,2,3,4,5,6,7,8]
# print(list_of_list[2])
list_of_list = [[1,2,3],[4,5,6],[1,4,8]]
# print(list_of_list)

# Flatten `list_of_list`
# print(list_of_list)
other = [y for x in list_of_list for y in x]
# print(other)



    #   0,0   0,1  1,0   1,1  
A = [[2,3],[3,4]]
B = [[4, 5],[7,2]]
# print(A)
# print(B)
supuesta_respuesta = [[6, 8], [10, 6]]
res = []
for i in range(2):
    for j in range(2):
        res.append(A[i][j] + B[i][j])
        
print(res)


suma_matrices = [A[i][j] + B[i][j] for i in range(2) for j in range(2)]
print(suma_matrices)




















