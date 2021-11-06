def my_gen():
    print("Hello amigo")
    n = 0
    yield n

    print("Aqui estoy")
    n = 1
    yield n
    
    print("De nuevo")
    n = 2
    yield n

a = my_gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a))




