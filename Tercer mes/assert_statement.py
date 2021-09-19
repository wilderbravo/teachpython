def palindromo(cadena):
    assert len(cadena)>0, "No se puede ingresar una cadena vacía"
    return (cadena==cadena[::-1])

cadena = ""
print(palindromo(cadena))