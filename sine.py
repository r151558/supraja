import matplotlib.pyplot as plt
import numpy as np
f1=100
f2=200
fs=3000
y=np.arange(0,100,1)
x1=np.cos(2*np.pi*y*f1/fs)
x2=np.cos(2*np.pi*y*f2)/fs
x=x1+x2
plt.stem(x)
plt.show()