# num = 100
# pares = [i for i in range(1,num) if i % 2 == 0]
# print(pares)

class NumerosPares():
    def __init__(self, numMax) -> None:
        self.max = numMax

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num +=2
            return result
        else:
            raise StopIteration

Mis_pares = NumerosPares(1000)
for elemento in Mis_pares:
    print(elemento)
