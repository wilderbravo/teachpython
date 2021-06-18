class Estudiante(object):  #Creamos la clase padre
    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre #Declaramos que el atributo nombre es igual al argumento nombre

class Instituto(object):
    def presentarinstituto (self):
        print("""Estudio en el Instituto de Leyes 112""")

class Derecho (Estudiante, Instituto): #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                            #Lo que la convierte a DERECHO en una clase hija o secundaria
    def presentarse(self): #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Derecho") #Se presenta llamando los atributos

    def cambiar_edad(self, edad):
        self.edad =edad
       
Manuel = Derecho(26, 'Manuel Contreras') #Indicamos argumentos edad y nombre
Manuel.presentarse() # Llamamos al método y Manuel se presenta
Manuel.presentarinstituto()
Manuel.cambiar_edad(32)
Manuel.presentarse() # Llamamos al método y Manuel se presenta
# sum(i*i for i in range(10))