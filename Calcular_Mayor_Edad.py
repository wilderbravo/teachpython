#Programa que me permite calcular si una persona es mayor de edad o no
nombre_persona = str(input("Por favor ingrese su nombre: "))#Pido el nombre de la persona
edad_persona = int(input(f"Por favor {nombre_persona} ingrese su edad: "))#Pido su edad
if edad_persona>=18:
    print(f"Amigo {nombre_persona} usted es mayor de edad, ya puede votar en las elecciones")
else:
    print(f"Lo sentimos mucho {nombre_persona} usted no puede sufragar porque es menor de edad")

print("Gracias...")

