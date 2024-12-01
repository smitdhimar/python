import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("C:/Users/91875/VScode/python/regression/data.csv")

#this is the set of independent variables
X=df[['Volume','Weight']];

#now scaling the independent variables
scaler=StandardScaler();
scaledX=scaler.fit_transform(X);
print()
print("scaled x: ")
print(scaledX)


#this is the dependent variable y
y=df['CO2']

model=linear_model.LinearRegression();
model.fit(scaledX,y)

coefOfVars=model.coef_
print("volume: ",coefOfVars[0])
print("weight: ",coefOfVars[1])


inputValues=pd.DataFrame([[2300,2300]] , columns=['Volume','Weight']);
predictedValue=model.predict(scaler.transform(inputValues));
print(predictedValue)

