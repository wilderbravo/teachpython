def divisors(num):
    try:
        if (num<0):
            raise ValueError("No se admiten números negativos")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError: #Es un error de tipo ValueError
        print("Debes ingresar un número")


# if __name__ == '__main__':
run()