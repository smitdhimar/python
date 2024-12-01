principle=[40000,50000,60000,70000,80000,90000,100000,110000,120000];
interest= [i*(1+(8.5/100))**3 for i in principle];
for i in principle:
    print(i*(1+(6/100))**20);
import matplotlib.pyplot as plt
plt.plot(principle,interest, label="principle vs interest");
plt.xlabel("principle")
plt.ylabel("principle with compouding interest")
plt.title("principle vs compuding interest")
plt.show();