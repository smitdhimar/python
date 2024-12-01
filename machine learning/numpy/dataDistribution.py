import numpy as np;
import matplotlib.pyplot as plt;
#this is the example of uniform distribution of data
data=np.random.uniform(0.1,1,1000)

# print(data);

# plt.hist(data)
# plt.show();

#in the following example i will explain about the normal distribution in which random values revolves around a single value;

normalData=np.random.normal(0.1,1,100000);
# plt.hist(normalData,100)
plt.scatter(normalData)
plt.show();