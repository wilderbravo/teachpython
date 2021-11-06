from datetime import datetime
from time import time

def counter(func):
    def decorador(*args, **kwargs):
        tiempo_inicio = datetime.now()
        func(*args, **kwargs)
        tiempo_final = datetime.now()
        diferencia = tiempo_final - tiempo_inicio
        print(f"El tiempo que tomó la función fue de {diferencia.total_seconds()}")
        print(f"Tiempo en que fue ejecutado {tiempo_inicio.hour}:{tiempo_inicio.minute}:{tiempo_inicio.second}")
    
    return decorador

@counter
def funcion1():
    mi_variable = 4245454547987878787854656*9897777777777777466467878745454545454
    print(mi_variable)

@counter
def random_func():
    for _ in range(1, 100000000):
        pass
@counter
def suma(a: int, b: int) -> int:
    return a + b

funcion1()
random_func()
suma(4, 5)