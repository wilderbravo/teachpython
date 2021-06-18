import random 
import time

def crear_mazo():
    arreglo = []
    for i in range(1,11):
        for j in ('T','N','R','B'):
            arreglo.append((str(i)+j))

    return arreglo

def barajar_cartas(mazo):
    random.shuffle(mazo)
    return mazo

def repartir_cartas(mazo):
    arreglo = []
    contador = 0
    for i in mazo:
        if (contador<5):
            arreglo.append(i)
            mazo.remove(i)
        else:
            break
            
        contador+=1

    return arreglo, mazo

def iniciar_juego(nombre1,nombre2,mazo_barajado):
    mazo_posterior = []

    for i in range(1, 5):
        print(f'Se reparten las cartas del juego {i}')
        time.sleep(3)
        cartas_jugador1, mazo_posterior = repartir_cartas(mazo_barajado)
        cartas_jugador2, mazo_posterior = repartir_cartas(mazo_posterior)
        mazo_barajado = mazo_posterior

        for i, j in zip(cartas_jugador1, cartas_jugador2):
            print(f'Jugador 1 {nombre1} lanza su carta {i} \n')
            print(f'Jugador 2 {nombre2} lanza su carta {j} \n')

        print('--'*20)