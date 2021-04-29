def traducir(i):
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    return switcher.get(i,"No existe traducción")
dia = int(input('Por favor ingrese un día de la semana: \n'))
# print(traducir(dia))
print (f"El día ingresado traducido al inglés es {traducir(dia)}")