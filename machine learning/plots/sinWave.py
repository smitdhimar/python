# from pylab import *
# x=linspace(0,6,100);
# plot(x,sin(x),"g--")
# show();

import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0,1.6,0.01);
# plt.figure(1);
x=np.arange(-5,5,0.1);
plt.plot(x,x*x+2*x+1, label="quadratic equation");
plt.plot(t,1+np.cos(2*np.pi*t), label="sine wave")
plt.plot(t,1+np.sin(2*np.pi*t), label="cosine wave");
plt.xlabel("time");
plt.ylabel("voltage");
plt.title("tiem vs voltage in x meter")
plt.grid()
legend=plt.legend()
plt.savefig("temp.png")

plt.show();

