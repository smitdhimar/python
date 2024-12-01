import numpy as np;
from scipy import stats as st;

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(f'mean speed is {np.mean(speed)}');
print(f'median speed is {np.median(speed)}');
print(f'mode of the speed array is {st.mode(speed)}')