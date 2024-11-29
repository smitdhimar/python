def multiplier_of(num):
    def func(n):
        return num*n;
    return func;

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))