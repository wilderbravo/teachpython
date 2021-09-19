import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def read():
    numbers = []
    ruta = THIS_FOLDER + "/archivos/numbers.txt"
    with open(ruta, "r", encoding="utf-8") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    ruta = THIS_FOLDER + "/archivos/names.txt"
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose",  "Rocío"]
    with open(ruta, "w",  encoding="utf-8") as f: # a para agregar texto al archivo
        for name in names: 
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()
    print("Hola")
    os.system("cls")
    print("Yes")