
def mergeD(d1,d2):
    for i in d2:
        if(i not in d1):
            d1[i]=d2[i];

d1={"name":"smit",
    "age":20};
d2={"role":"sde1",
    "place":"role"};
mergeD(d1,d2);
print(d1)