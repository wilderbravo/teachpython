
# frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
# for nombre, color in frutas.items():
#     print (f"{nombre}, es de color {color}")
lista_datos1 = [{'Nombres':'Wilder', 'Apellidos':'Bravo'}, {'Nombres':'Anthony', 'Apellidos':'Bravo C'}]
cadena = ''
print("--"*60)
print(lista_datos1)
contador = 0

while contador<5:
    cadena = {'Nombres':'Nombre ' + str(contador), 'Apellidos':'Cedeño'+ str(contador)}
    lista_datos1.append(cadena)
    contador+=1

print("--"*60)
print(lista_datos1)
print("--"*60)
print(lista_datos1[5])


