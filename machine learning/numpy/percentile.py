#this is the program to find a number from the array which has percentile given as the argument

import numpy as np

speed=[34,87,4,23,53,6,457,34,68]
thatNumber=np.percentile(speed,0)
print(thatNumber)

