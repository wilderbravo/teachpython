import re



def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto) )
#Prueba 1 
patrones = ['hola', 'hoola']
texto = "hola hla hol hooola hoola hola hoooooooola hoola hoola hoola"
buscar(patrones, texto)

print("--"*50)
#Prueba 2
texto = "hola h0la Hola mola m0la M0la sopa gat9"
patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}', 'gat[0-9]'] 
buscar(patrones, texto)

#Prueba 3
print("--"*50)
hora = "24:05 PM"
patrones = ['^[0-9]{2}:[0-9]{2} AM|PM$']

buscar(patrones, hora)

#Prueba 4
texto = "40 + 8 / 25"
patrones = ['^[0-9]{1,2} \+ [0-9]{1,2} / [0-9]{1,2}$']
buscar(patrones, texto)

#Prueba 5
print('--'*50)
texto = "(45 * 5^2) / (67 - 25 * 6)"
texto1 = "(45 * 5 / 2)"
texto2 = "(67 - 25 * 6)"
patron1 = ['^\([0-9]{1,2} \* [0-9]{1,2} / [0-9]{1,2}\)$']
patron2 =['^\([0-9]{1,2} - [0-9]{1,2} \* [0-9]{1,2}\)']
patron = ['^\([0-9]{1,2} \* [0-9]{1,2} / [0-9]{1,2}\) / \([0-9]{1,2} - [0-9]{1,2} \* [0-9]{1,2}\)$']

buscar(patron1, texto1)
buscar(patron2, texto2)
buscar(patron, texto)