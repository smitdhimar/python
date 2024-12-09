#import statements
#pandas
import pandas as pd
#numpy
import numpy as np
#matplotlib.pyplot for plotting the graphs
import matplotlib.pyplot as plt
# r2 scores for measurement of relation
from sklearn.metrics import r2_score;
#importing the train test split
from sklearn.model_selection import train_test_split
# to preprocess the columns
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn import metrics
#this dataset is about the effort vs sales data. the marketing done on tv, radio, news paper and it's impact on sales.
#creating data frame
df=pd.read_csv("C:/Users/91875/VScode/python/machine learning/regression/advertisingRegerssionPlay/advertising.csv")

# splitting the dataset into the independent and dependent variables
X=df[['TV','Radio','Newspaper']]
y=df['Sales']

#preprocessing
scaler=StandardScaler();
scaledX=scaler.fit_transform(X)


#splitting the dataset for training and testing
trainX,testX,trainY, testY=train_test_split(scaledX,y,shuffle=True, test_size=0.25)

#model initialization 
model=linear_model.LinearRegression()
#model fitting
model.fit(trainX,trainY)
#prediction
# inputValue=pd.DataFrame([[240,25,46]],columns=['TV','Radio','Newspaper'])
# prediction=model.predict(scaler.transform(inputValue))

# prediction
y_pred=model.predict(testX)
# r2score
print("r2 score beetween y_pred and y_test is : ", r2_score(y_pred,testY))


print("training accuracy: ",model.score(trainX,trainY))
print("testing accuracy: ", model.score(testX,testY))

# plotting 
# plt.plot(X,y)
# plt.scatter(X,y)
# plt.show()