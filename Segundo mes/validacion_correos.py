import os
import re
import mysql.connector
import datetime

body_regex = re.compile('''
    ^(?!\.)                            
    (
    [-a-z0-9!\#$%&'*+/=?^_`{|}~]     
    |
    (?<!\.)\.                        
    )+
    (?<!\.)$                           
''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''
    (
    localhost
    |
    (
        [a-z0-9]
        (
        [-\w]*                         
        [a-z0-9]                       
        )?
    \.                               
    )+
    [a-z]{2,}                        
)$
''', re.VERBOSE | re.IGNORECASE)

def is_valid_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False
    body, domain = email.rsplit('@', 1)
    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)

def cargar_correos():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'correos.csv')
    count = 0
    #Declaración de lista para almacenar correos
    correos = []
    xfile = open(my_file)
    for texto in xfile:
        arreglar_texto = texto[0:-1].split(",")
        correos.append(arreglar_texto[1])
        count = count + 1
    
    return correos

def conectar():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    database="Correos"
    )

    return mydb

def insertar_correos(lista_correos):
    mydb = conectar()
    mycursor = mydb.cursor()
    contador = 1
    tiempo = datetime.date.today()
    # Solo insertar correos válidos
    for correo in lista_correos:
        if (is_valid_email(correo)):
            contador=contador+1
            mycursor.execute(f"insert into correos_validos values({contador}, '{correo}','{tiempo}');")
    
    mydb.commit()
    print("Datos agregados con éxito!")

lista_correos = cargar_correos()
insertar_correos(lista_correos)
