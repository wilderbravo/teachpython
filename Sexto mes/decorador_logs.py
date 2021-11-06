import os
from datetime import datetime

def log_function(func):
    def log(*args, **kwargs):
        # Manejo de archivos
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'file.log')
        # Guardado del log
        date = datetime.now()
        xfile = open(my_file, "a")
        output = func(*args, **kwargs) # suma, resta, multipica, divide
        print(output)
        xfile.write(f"Log-{func} Resultado: {output} creado en la fecha {date} \n")
        xfile.close
    
    return log

@log_function
def suma(a: int, b:int) -> int:
    return (a + b)

@log_function
def resta(a: int, b:int) -> int:
    return (a - b)

@log_function
def multiplica(a: int, b:int) -> int:
    return (a * b)

@log_function
def divide(a: int, b:int) -> float:
    assert b != 0, "No se puede dividir para 0"
    return (a / b)

suma(5,6)
resta(18,3)
multiplica(5,100)
divide(100,3)

