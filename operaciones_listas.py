#Archivo de operaciones con listas
mi_lista = []
for i in range(0,5):
    mi_peticion = int(input(f"Por favor ingrese el numero {i+1}: \n"))
    mi_lista.append(mi_peticion)


print(f"La lista tiene los siguientes valores: \n {mi_lista}")
