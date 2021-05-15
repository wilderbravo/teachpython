def cuenta_regresiva(numero):
    numero -= 1
    # numero = numero -1
    if numero > 0:
        print (numero)
        cuenta_regresiva(numero)
    else:
        print ("Boooooooom!")

    # print (f"Fin de la función {numero}")

cuenta_regresiva(5)

# def cuenta_regresiva(numero):
#     print(numero)
#     for i in range (1, numero):
#         print(numero-i)

# cuenta_regresiva(10)