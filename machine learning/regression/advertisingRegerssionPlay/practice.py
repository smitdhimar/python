import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/91875/VScode/python/machine learning/regression/advertisingRegerssionPlay/advertising.csv")

#returns tuple containing number of rows, columns of dataset
print(df.shape)

#returns the datastructure whether the any column consists any empty cell or not 
print(df.isna().any())

#returns the data types of all columns .
print(df.dtypes)

#plotting multiple graphs on single canvas
fig,axs=plt.subplots(1,3,sharey=True)
df.plot(kind='scatter',x='TV',y='Sales',ax=axs[0])
df.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
df.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])
plt.show()

feature_x=['TV','Radio','Newspaper']
X=df[feature_x]
y=df.Sales
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
xtrain,xtest,ytrain,ytest=model_selection.train_test_split(X,y,test_size=0.3,random_state=30)
print(xtrain.shape,ytrain.shape,xtest.shape,ytest.shape)

lm=LinearRegression()
lm.fit(xtrain,ytrain)
preds=lm.predict(xtest)


print(" accuracy: ", lm.score(xtrain,ytrain))


# got the accuracy same as i did in main.py