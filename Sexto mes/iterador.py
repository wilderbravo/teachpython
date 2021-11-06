my_list = [1, 2, 3, 4, 5]
print(type(my_list))

# for elemento in my_list:
#     print (elemento)

my_iter = iter(my_list)
print(type(my_iter))

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

for elemento in my_list:
    print (elemento)