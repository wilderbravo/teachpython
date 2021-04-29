# Importar archivos
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(THIS_FOLDER)
my_file = os.path.join(THIS_FOLDER, 'file.txt')
count = 0
print(my_file)
#Declaración de lista
mis_sitios = []
xfile = open(my_file)
for texto in xfile:
    arreglar_texto = texto[0:-1]
    # print(arreglar_texto)
    mis_sitios.append(arreglar_texto)
    count = count + 1
print (count)

print("--"*100)
print(f"Mis sitios : {mis_sitios}")

# mi_variable = '@abcdefg8234'
# print(mi_variable[0:-2])
