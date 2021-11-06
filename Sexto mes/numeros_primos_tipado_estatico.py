"""
Programa de Python que permite conocer si un número es primo 
o no, mediante el tipado estático
"""
def es_primo(number: int) -> bool:
    print("Hola")
    resultado_lista = [x for x in range(2, number) if number % x ==0]
    return len(resultado_lista) == 0

def es_primo_dinamico(number):
    print("Hola")
    resultado_lista = [x for x in range(2, number) if number % x ==0]
    return len(resultado_lista) == 0

def main():
    number = "10"
    numero_es_primo: bool = es_primo(number)
    # numero_es_primo_dinamico = es_primo_dinamico(number)
    print(f'Es {number} un número primo: {numero_es_primo}')
    # print(f'Es {number} un número primo: {numero_es_primo_dinamico}')

main()
