from Archivo_funciones import *

#Datos para inicializar el juego
cartas_jugador1 = []
cartas_jugador2 = []

nombre1 = str(input('Por favor ingrese el nombre del primer jugador: \n'))
nombre2 = str(input('Por favor ingrese el nombre del segundo jugador: \n'))

mazo_inicial = crear_mazo()
print(f'El mazo inicial tiene las siguientes cartas: \n\n {mazo_inicial} \n\n')
mazo_barajado = barajar_cartas(mazo_inicial)
print(f'El mazo barajado queda de la siguiente manera: \n\n {mazo_barajado} \n\n')

iniciar_juego(nombre1,nombre2,mazo_barajado)


