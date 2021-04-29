# Diccionarios
mi_diccionario = {'nombre' : 'Ariosto', 'edad' : 12, 'cursos': ['Python','Django','JavaScript'] }

print(mi_diccionario)

print (mi_diccionario['nombre'])
print (mi_diccionario['edad'])
print (mi_diccionario['cursos'])

print (mi_diccionario['cursos'][0])
print (mi_diccionario['cursos'][1])
print (mi_diccionario['cursos'][2])
print("--"*50)
for key in mi_diccionario:
  print (key, ":", mi_diccionario[key])

# Métodos de los diccionarios
print("--"*50)
#representación de un diccionario -  diccionario de datos
dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)
print(dic)

print("--"*50)
dic = dict(zip('abcd',[1,2,3,4]))
print(dic)

print("--"*50)
dic = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
items = dic.items()
print(items)

print("--"*50)
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}# Clave: Valor
keys= dic.keys()
print(keys)

print("--"*50)
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
values= dic.values()
print(values)

print("--"*50)
dic1 =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic1.clear()
print(dic1)

print("--"*50)
dic1 =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic2 = dic1.copy()
print(dic2)

print("--"*50)
dic = dict.fromkeys(['gato','oso','perro','tigre'],5)
print(dic)

print("--"*50)
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
valor = dic.get('d') 
print(valor)

print("--"*50)
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
valor = dic.pop('b')
print(dic) 

print("--"*50)
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
# valor = dic.setdefault('a')
# print(valor) 
valor = dic.setdefault('e',5)
print(dic)

print("--"*50)
dic =  {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
dic.update(dic2)
print(dic)




