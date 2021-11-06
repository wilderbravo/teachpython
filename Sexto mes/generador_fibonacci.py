import time

def fibo_gen(numMax: int):
    n1, counter = 0, 0
    n2 = 1 

    while True:
        if counter == 0:
            counter += 1
            yield n1 
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux >= numMax:
                print("Finalizado!")
                break
            n1, n2 = n2, aux
            counter += 1
            yield aux

fibonacci = fibo_gen(50)
for elemento in fibonacci:
    print(elemento)
    # time.sleep(1)