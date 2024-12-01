import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score;
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("C:/Users/91875/VScode/python/machine learning/regression/advertisingRegerssionPlay/advertising.csv")

X=df[['TV','Radio','Newspaper']]
y=['Sales']

plt.plot(X,y)
plt.scatter(X,y)
plt.show()
# print(df.head(8))