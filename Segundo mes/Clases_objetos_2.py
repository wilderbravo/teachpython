class Mascota():
    def __init__(self, nombre, especie):
        self.nombre=nombre
        self.especie=especie
    
    def presentarAnimal(self):
        print(f"El animal {self.nombre} pertenece a la especie {self.especie}")

    def darNombre(self, nombre):
        self.nombre=nombre

    def darEspecie(self, especie):
        self.especie=especie

class Perro(Mascota):
    def __init__(self, nombre, raza, color, persigue_gatos):
        Mascota.__init__(self, nombre, "Perro")
        self.raza=raza
        self.color=color
        self.persigue_gatos=persigue_gatos
    
    def persigueGatos(self):
        return self.persigue_gatos

animal1 = Mascota("gato","felinos")
animal1.presentarAnimal()
animal1.darNombre("pantera")
animal1.presentarAnimal()
print("-"*80)
mascota = Mascota("Falucho", "Perro")
perro = Perro("Falucho", "Negro", "Boxer", True)

print(perro.persigueGatos())