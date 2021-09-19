import requests  #Importamos la librería requests

print("Solicitando información de la web")
print("Espere....") 
URL = 'https://restcountries.eu/rest/v2/all' #configuramos la url
# URL = 'https://reqres.in/api/users?page=2'
# URL = 'https://api.covidtracking.com/v1/states/ca/info.json'
#solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL) 

data = data.json() #convertimos la respuesta en dict

for paises in data:
    # print(paises)
    print(f"Pais: {paises['name']}({paises['alpha3Code']}) == Capital: {paises['capital']} == Poblacion: {paises['population']} ") 
