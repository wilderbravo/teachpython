class Automovil():
    def __init__(self, marca, color, cilindraje, rin, gasolina):
        self.marca=marca
        self.color=color
        self.cilindraje=cilindraje
        self.rin=rin
        self.gasolina=gasolina
    
    def arrancar(self):
        if (self.gasolina>0):
            print("Arrancar")
        else:
            print("No arrancas")
    
    def llenarGasolina(self, gasolina):
        self.gasolina=gasolina

    def conducir(self):
        if (self.gasolina>0):
            self.gasolina -=1
            print(f"Te queda {self.gasolina} de litros de gasolina")
        else:
            print("No se puede mover, no hay gasolina")

    def presentar(self):
        print(f"El automóvil {self.marca} es de {self.cilindraje} cc, color {self.color} con rin tamaño {self.rin}")

mi_coche = Automovil("Chevrolet","Blanco",1500, 15, 5)
mi_coche.presentar()
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
mi_coche.llenarGasolina(1)
mi_coche.conducir()
mi_coche.conducir()
