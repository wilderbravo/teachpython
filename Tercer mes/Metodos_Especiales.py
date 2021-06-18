class Galleta():
    #Atributos
    chocolate = False 

    #Constructor de la clase
    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    #Destructor de la clase
    def __del__(self):
        print("La galleta se está borrando de la memoria")

    def presentarse(self):
        print(f"Hola soy una galleta crocante de sabor a {self.sabor} y de color {self.color}")
    
    def cambio_color_externo(self, color):
        self.__cambio_color_interno(color)

    #Método de uso interno
    def __cambio_color_interno(self, color):
        self.color = color

objeto_galleta = Galleta("Vainilla","Gris")
objeto_galleta.presentarse()
objeto_galleta.cambio_color_externo("Negro")
objeto_galleta.presentarse()
del(objeto_galleta)
# objeto_galleta = Galleta("Vainilla","Gris")
# objeto_galleta.presentarse()
