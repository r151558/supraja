import numpy as np
import  matplotlib.pyplot as plt
m=32
n=np.arange(0,31)
h=0.54-0.46*np.cos(2*np.pi*n/(m-1))
plt.stem(n,h)
plt.show()