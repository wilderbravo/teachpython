# 0, 1, 1, 2, 3, 5, 8, 13
import time

class FiboIter():
    def __init__(self, numMax=1000000000):
        self.numMax = numMax
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0

        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux >= self.numMax:
                print("Finalizado!")
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

fibonacci = FiboIter(100)
for elemento in fibonacci:
    print(elemento)
    time.sleep(1)