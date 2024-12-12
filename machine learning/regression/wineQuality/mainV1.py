import pandas as pd;
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
#loading the dataset
dataset=pd.read_csv('C:/Users/91875/VScode/python/machine learning/regression/wineQuality/winequalityRed.csv')


# print(dataset.shape)
# returned 1599,12

# print(dataset.isna().any())
# returned false for all
 
# print(dataset.dtypes)
# returned all the datatypes

#checking if there are any empty cell in certain columns
# print(dataset.isnull().sum())

#feeling all the null values with mean
for col in dataset.columns:
    if(dataset[col].isnull().sum()>0):
        dataset[col]=dataset[col].fillna(dataset[col].mean())



X=dataset[dataset.columns[0:11]]
scaler=MinMaxScaler();

# splitting the x and y
ScaledX=scaler.fit_transform(X);
y=dataset[dataset.columns[11]]

#splitting into train x , train y , test x, test y .
trainX,testX,trainY, testY=train_test_split(ScaledX,y,test_size=0.25,shuffle=True, random_state=40)

lrModel=linear_model.LinearRegression();
lrModel.fit(trainX,trainY)

y_pred=lrModel.predict(testX)
print("r2 score between the y_pred and testY is : ", r2_score(y_pred,testY))

print("training accuracy: ", lrModel.score(trainX,trainY))
print('testing accuracy: ', lrModel.score(testX,testY))

 

#got bad accuracy