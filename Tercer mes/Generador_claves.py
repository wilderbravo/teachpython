# Realizar un programa para que genere claves potentes de 12 caracteres
import random
import array

class Clave():
    def __init__(self, longitud):
        self.longitud = longitud

    def generar_contrasena(self):
        DIGITOS = ['0','1','2','3','4','5','6','7','8','9','0']
        MINUSCULAS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        MAYUSCULAS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        SIMBOLOS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

        LISTA_COMBINADA = DIGITOS + MAYUSCULAS + MINUSCULAS + SIMBOLOS
        
        rand_digitos = random.choice(DIGITOS)
        rand_mayus = random.choice(MAYUSCULAS)
        rand_minus = random.choice(MINUSCULAS)
        rand_simbolos = random.choice(SIMBOLOS)

        temp_pass = rand_digitos + rand_mayus + rand_minus + rand_simbolos

        for x in range(self.longitud -4):
            temp_pass = temp_pass + random.choice(LISTA_COMBINADA)
            temp_pass_list =  array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        
        password = ''

        for i in temp_pass_list:
            password = password + i
        
        return password
        

Datos = Clave(32) # Instanciar la clase
contrasena_generada = Datos.generar_contrasena()
print(f"La contrasena generada es {contrasena_generada}")