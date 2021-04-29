# Números aleatorios
# https://unipython.com/numeros-aleatorios-modulo-random/

import random
for x in range(10): 
    print (random.randint(0,20))

print("--"*100)
print (random.randint(10,30))

print("--"*100)
print (random.random()*50)

print("--"*100)
color=random.choice( ['rojo', 'amarillo', 'verde', 'azul', 'morado'])
print(color)

print("--"*100)
s=list(range(15))
random.shuffle(s)
print(s)

print("--"*100)
print(random.randrange(0,50,2))

#Números impares del 1 al 35
print("--"*100)
print(f"Impar: {random.randrange(1,36,2)}")
print("--"*100)

print("--"*100)
str1 = "L4wisdom.com"
list1= ['a','b','c','d','e','f','o','l']
print (random.sample(str1,4))
print (random.sample(str1, len(str1)))
print("--"*100) 
 