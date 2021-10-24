FORMAT_PHONE = 'e+0000000000'

def getPhone() -> int:
    # phone = input('Ingrese su teléfono: ')
    phone = input(str('Ingrese su teléfono: '))
    if not phone:
        return FORMAT_PHONE.round()
    else:
        return int(phone)

def run():
    my_phone = getPhone()
    print(f'Tu teléfono es {my_phone}')

# run()

# Python tiene un tipado dinámico y fuerte
# x = 1
# y = "2"
# z = x + y

# print(z)

# # Ejemplo 
# # Javascript es un lenguaje de tipado débil

# const x = 1;
# const y = "2";
# const z = x + y; # 12

# # //Hace un cast del 1 en string para combinarlos, resultado = 12

# #Php
# $str = 5 + "5" # 10
#//Cast el "5" a entero y lo suma, resultado 10

