import random

def evaluar(valor1, valor2):
    lista = {"Piedra":1, "Papel":2, "Tijera":3}
    if (lista[valor1]==lista[valor2]):
        return 0,0
    if (lista[valor1]>lista[valor2]):
        return 0, 

datos = ["Piedra","Papel","Tijera"]

usuario1 = input(str("Usuario 1, Ingrese su nombre: "))
usuario2 = input(str("Usuario 2, Ingrese su nombre: "))

for i in range(5):
    print(f"Ronda No {i+1} \n")
    random.shuffle(datos)
    elegido1 = random.choice(datos)
    print(f"{usuario1} saca {elegido1}")

    random.shuffle(datos)
    elegido2 = random.choice(datos)
    print(f"{usuario2} saca {elegido2} \n")

    # evaluar(elegido1, elegido2)