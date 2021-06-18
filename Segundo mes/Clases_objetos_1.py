class Humano(): #Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion): 
        # Definición de atributos
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion

    # Definición de métodos o eventos
    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") #Mensaje
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos 

    def contratar(self, puesto): #añadimos un nuevo parámetro en el método
        self.puesto = puesto
        print ("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.ocupacion = puesto #Ahora cambiamos el atributo ocupación

# Ejecución del ejercicios
Persona1 = Humano(31, "Pedro", "Bombero") #Instancia
# Persona2 = Humano(38, "Luis", "Ingerniero") #Instancia
Persona1.presentar() 
Persona1.contratar("Obrero")
Persona1.presentar()