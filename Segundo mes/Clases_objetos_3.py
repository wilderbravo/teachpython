class Operaciones():
    def __init__(self, parametro1, parametro2):
        self.parametro1=parametro1
        self.parametro2=parametro2
    
    def sumar(self):
        return self.parametro1+self.parametro2
    
    def restar(self):
        return self.parametro1-self.parametro2

    def multiplicar(self):
        return self.parametro1*self.parametro2

    def dividir(self):
        return self.parametro1/self.parametro2

calculo1 = Operaciones(5, 4)

print(calculo1.sumar())
print(calculo1.dividir())