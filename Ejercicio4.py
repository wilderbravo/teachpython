import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6) 

# print (f"El dado se ha girado: {dado}")

suma = dado1 + dado2

print(f"Dado 1: {dado1}, Dado 2: {dado2}, suma: {suma} ")

if (suma>=2 and suma<=6):
    print("Rango de perdedor")
else:
    print("Rango de ganador")