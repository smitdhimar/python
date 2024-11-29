#write a function to reverse a string using recursion


def func(str,n):
    if(n==0):
        return "";
    return str[n-1]+func(str,n-1);


print(f"reverse of the string Hello world is {func("Hello world",11)}")
