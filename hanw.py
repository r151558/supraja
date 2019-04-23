import numpy as np
import matplotlib.pyplot as plt
m=32
n=np.arange(0,31)
h=0.5-0.5*np.cos(2*np.pi*n/31)
plt.stem(n,h)
plt.show()
