def factorial(numero):
    # print (f"Valor inicial -> {numero}")
    if numero > 1:
        numero = numero * factorial(numero -1)
    # print (f"valor final -> {numero}")
    
    return numero

factorial_numero = factorial(1000)
print(f"El factorial del numero es {factorial_numero}")
