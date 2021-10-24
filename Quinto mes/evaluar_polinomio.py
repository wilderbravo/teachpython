# x^4+x^3+2x^2-x
# def evaluar(x):
#     return ((x**4)+(x**3)+(2*x**2)-x)
# import matplotlib.pyplot as plt

def evaluar1(x):
    return (x**4) + (x**3) + (0.5 * x ** 2) - x

numerosPares = [i for i in range(1,22) if i % 2 == 0]
ejes_y = [evaluar1(c) for c in numerosPares]

print(numerosPares)
print(ejes_y)
