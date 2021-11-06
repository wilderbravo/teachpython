def make_repetear_of(n):
    def repeater(cadena):
        assert type(cadena) == str, "Solo puedes utilizar cadenas"
        return (cadena + " ") * n

    return repeater

repetir = make_repetear_of(5)
cadena_repetida = repetir("Hola")

print(cadena_repetida)