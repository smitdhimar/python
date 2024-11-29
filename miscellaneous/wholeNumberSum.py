def whole(num):
    sum=0
    for i in range(0,num+1):
        sum+=i;
    return sum;

def whole2(num):
    if num==0:
        return 0;
    return num+whole2(num-1);
print(whole2(10));