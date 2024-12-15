#required imports
import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score;
from sklearn.ensemble import RandomForestClassifier;
from sklearn.model_selection import train_test_split;

#loading dataset
dataset=pd.read_csv('./customerChurnDS.csv')

# print(dataset.isna().sum());
# analysis of data
# print(dataset.dtypes)
# print(dataset.head())
# print(dataset.describe())

#inference from analysis of data
# 1. it seems that customer id is the id which should not affect the dataset analysis
# 2. the problem is for classification
# 3. There are 3 columns named gender, subscription type, Contract Length which needs to be converted to 0..1

#dropping the not required column
dataset.drop('CustomerID',axis=1,inplace=True);

#converting gender column values to 0..1
dataset['Gender']=dataset['Gender'].apply(lambda x:1 if x=='Male' else 0)
#converting Subscription Type column
dataset['Subscription Type']=dataset['Subscription Type'].apply(lambda x: 0 if x=='Basic' else 1 if x=='Standard' else 2);
#converting Contract Length column
dataset['Contract Length']=dataset['Contract Length'].apply(lambda x: 0 if x=='Monthly' else 1 if x=='Quarterly' else 2);

#dropping the na columns 
dataset.dropna(inplace=True)
#correlation
# correlation=dataset.corr();

#visuallization of data
#heat map
# sns.heatmap(correlation,cmap='Greens',cbar=True,fmt='.1f',annot=True);
sampleDS=dataset.sample(n=100);
sns.pairplot(sampleDS,hue="Churn")
plt.show()

#x,y
X=dataset.drop('Churn',axis=1)
y=dataset['Churn'];

# splits
trainX,testX,trainY,testY=train_test_split(X,y,test_size=0.2);

# model initiallization
model=RandomForestClassifier();

#training
model.fit(trainX,trainY)

# prediction of testX
predY=model.predict(testX)
print("accuracy: ", accuracy_score(predY,testY));