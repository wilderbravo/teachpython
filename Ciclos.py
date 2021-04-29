contador = 0
for i in range(1,11):
    print(f"Suma de {contador} + {i} es = ")
    contador += i
    print(contador)

print (contador)

lista = [2, 4, 5, 6 , 7, 8, 5, 3, 15, 17, 18, 35, 44]
operacion = 0
contador = 0
for i in lista:
    operacion = i % 2
    if (operacion==0):
        contador+=1

print(f"Dentro de la lista hubo {contador} numeros pares")
