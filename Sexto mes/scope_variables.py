# #Ejer 0
# num = 4
# def my_func(num):
#     mi_var = 5
#     print(num, mi_var)
#     return mi_var

# print(my_func(num))


# Ejer 1
# num = 6

# def my_func():
#     print(num)

# def otra_func():
#     print(num)

# my_func()
# otra_func()

#Ejer 2
# z = 6

# def my_func1():
#     z=5
#     print(z)

# def otra_func1():
#     print(z)

# my_func1()
# otra_func1()

#Ejer 2
z = 6

def my_func1():
    z=5

    def my_func_other():
        z = 2 
        print(z)
    
    my_func_other()
    print(z)

my_func1()
print(z)