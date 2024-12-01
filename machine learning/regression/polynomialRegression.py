import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# this returns the coefficients of equation 
coefficients=np.polyfit(x,y,3)

print(coefficients)

# poly1d is a class and instances an object;
mymodel=np.poly1d(coefficients)

newx=np.linspace(1,22,100)
plt.plot(x,y)
plt.scatter(x,y)
plt.plot(newx,mymodel(newx))


print(r2_score(y,mymodel(x)));
plt.show()