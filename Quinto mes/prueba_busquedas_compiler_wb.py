import re

url = re.compile(r"^(https?://)?([da-z.-]+).([a-z]{2,6})([/w .-]*)*/?$")

if url.search("https://pythondiario.1com/"): # Comprobemos que esta es una URL valida
    print("URL Valida")
else:
    print("URL No Valida")