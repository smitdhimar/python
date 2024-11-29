import numpy as np;
l=[1,4,2,4,32,5,245,2345,43,2345,5];
def uniqueE(l):
    l=np.unique(l);
    l.sort();
    return l;

print(uniqueE(l));