def make_multiplier(x):

    def multiplier(n):
        return n*x
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times10(2))
print(times4(3))
print(times4(10))