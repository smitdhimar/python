#importing all the required libraries
import numpy as np;
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier;
import seaborn as sns;
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt;

#loading the data
dataset=pd.read_csv('./winequalityRed.csv')

#Analysis of data
# print(dataset.describe())

correlation = dataset.corr();
sns.heatmap(correlation,cmap='Greens',cbar=True, annot=True,fmt='.1f')
plt.show();

#classifiying the dataset
X=dataset.drop('quality',axis=1, inplace=False);
y=[ 1 if x>=7 else 0 for x in dataset['quality']];

#split
trainX,testX,trainY,testY=train_test_split(X,y,test_size=0.2, random_state=3)

model=RandomForestClassifier();
model.fit(trainX,trainY)
y_pred=model.predict(testX)
print(accuracy_score(y_pred,testY))
