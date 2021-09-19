def palindromo(cadena):
    try:
        if(len(cadena)==0):
            raise ValueError("No se admiten cadenas vacías")
        return (cadena==cadena[::-1])
    except ValueError as ve:
        print(ve)
        return False

cadena = ""
print(palindromo(cadena))
# finally trabaja con except para control de errores, ejemlpo cierre de un archivo o conexión a BD en caso 
# de presentarse un error 
