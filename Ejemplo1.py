def week(i):
    switcher={
        0:'Domingo',
        1:'Lunes',
        2:'Martes',
        3:'Miércoles',
        4:'Jueves',
        5:'Viernes',
        6:'Sábado'
    }
    return switcher.get(i,"Parámetro no existe")

print (f"El día de la semana es {week(3)}")