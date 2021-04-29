# -*- coding: utf-8 -*-
import os
import random
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(THIS_FOLDER)
my_file = os.path.join(THIS_FOLDER, 'Animales.txt')
count = 0
print(my_file)
#Declaración de lista vacía
mis_animales = []
xfile = open(my_file)
for texto in xfile:
    arreglar_texto = texto[0:-1]
    # print(texto)
    # print(arreglar_texto)
    mis_animales.append(arreglar_texto)
    count = count + 1
print (count)

print(mis_animales)
animal_seleccionado = random.choice(mis_animales)

print(f"Mi animal seleccionado es {animal_seleccionado}")