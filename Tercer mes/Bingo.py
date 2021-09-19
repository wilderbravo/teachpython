import random
palabras_compuestas = ['Bla','Ble','Bli','Blo','Blu','Cla','Cle','Cli','Clo','Clu','Fla','Fle','Fli','Flo','Flu','Gla',
'Gle',
'Gli',
'Glo',
'Glu',
'Tla',
'Tle',
'Tli',
'Tlo',
'Tlu',
]
c = 1
for i in range(4):
    random.shuffle(palabras_compuestas)
    grupo = [x for x in palabras_compuestas[:8]]
    print(f"Grupo {c}: {grupo}")
    c+=1

import Modulo
Modulo.mi_funcion()