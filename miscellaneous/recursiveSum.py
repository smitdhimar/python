#this is the program to find the recursive sum of the given nested list;

l=[5,1,[3,3,0,[5,6]],[2,5]];

def recursiveSum(l):
    sum=0;
    for i in l:
        if(type(i)!=int):
            sum+= recursiveSum(i);
        else:
            sum+=i;
    return sum;

print(recursiveSum(l));

