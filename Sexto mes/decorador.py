def decorador(func):
    def envoltura():
        print("Hola estoy agregando algo a tu función")
        func()
    
    return envoltura

@decorador
def saludo():
    print("Hola amigos")

@decorador
def suma():
    print(f"Mi suma {7+5}")

# saludo()
suma()
# saludo = decorador(saludo)

