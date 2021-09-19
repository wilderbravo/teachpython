#             Retorna un objeto de tipo función              
palindromo =  lambda cadena: cadena == cadena[::-1]

def palindromo1(cadena):
    return cadena==cadena[::-1]

cadena = "anas"
print(palindromo(cadena))
print(palindromo1(cadena))

# numbers = [1,2,3,4,5,6,7,8,9]
numbers = [a for a in range(1, 10)]
print(numbers)

from functools import reduce
list = [x*x for x in numbers]
# print(list)
all = reduce(lambda a, b: a+b, [a for a in range(1, 101)]) # Multiplicar todos los números de una lista
print(all)

# print("*"*10)
# lam = list(lambda x: x**2, numbers)
# # lam = lambda x**2: x, numbers
# print(lam)