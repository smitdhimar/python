# a = 1
# b = 2
# a, b = b, a
# print(a, b)

def fibo():
    a,b=1,1
    while(1):
        yield a
        a,b=b,a+b
        print
        
l=fibo()
i=0
for x in l:
    i+=1;
    print(x)
    if(i==10):
        break;