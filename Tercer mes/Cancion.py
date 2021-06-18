class Cancion:
    #Métodos especiales

    #Constructor
    def __init__(self, autor, titulo, duracion):  # en segundos
        self.duracion = duracion

    #Destructor
    def __del__(self):  
        print("El objeto se ha borraod de memoria")

    #Longitud
    def __len__(self):
       return self.duracion

cancion = Cancion("Queen", "Don't Stop Me Now", 210)

print(len(cancion))
print(cancion.__len__())