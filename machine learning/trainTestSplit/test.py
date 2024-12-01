import numpy as np
import pandas as pd;
from  sklearn.metrics import r2_score
import matplotlib.pyplot as plt
np.random.seed(2)

#creating the random value array
x=np.random.normal(3,1,100)
y=np.random.normal(150, 40 , 100)/x

#trainig data 
trainX=x[:80]
trainY=y[:80]

#testing data
testX=x[80:]
testY=y[80:]

#applying polynomial regression of degree 3
model=np.poly1d(np.polyfit(trainX,trainY,4))

#creating new array for target
new_x=np.linspace(0,6,100)
new_y=model(new_x)

#plotting
plt.scatter(trainX,trainY)
plt.plot(new_x,new_y)
plt.show()

#getting the r2 score between the 
score= r2_score(trainY, model(trainX))
print(score)
score= r2_score(testY, model(testX))
print(score)

#prediction 
print(model(2))