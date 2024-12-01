import numpy
from scipy import stats
import  matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
tup=stats.linregress(x,y)

# y=mx+c
# tup[0] is the slope which is the first element of the returned tuple  
# while the tup[1] is the intercept 
dependentVar=lambda i:i*tup[0]+tup[1];
y=[dependentVar(i) for i in x];

newy=dependentVar(10);
plt.scatter(10,newy,color="red")
plt.plot(x,y)
plt.show();
print(newy)

# plt.show();