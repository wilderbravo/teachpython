RISTRA_DE_CAJAS = ["BLANCO", "ROJO", "NEGRO"]

def funcion_generadora(ristra_de_cajas):
    for caja in ristra_de_cajas:
        if caja == "BLANCO":
            yield "AZUL"
        elif caja == "ROJO":
            yield "MORADO"
        else:
            yield caja

mi_var = funcion_generadora(RISTRA_DE_CAJAS)
for i in mi_var:
    print(i)