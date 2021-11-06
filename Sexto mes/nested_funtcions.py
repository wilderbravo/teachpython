def main():
    a = 1

    def nested():
        print(a)
    
    return nested

my_func = main()
# del(main)
# my_func1 = main()
my_func()