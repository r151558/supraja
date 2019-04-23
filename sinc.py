import numpy as np
import matplotlib. pyplot as plt
wc=np.pi/4
m=np.arange(-100,100,1)
h=(np.sin(wc*m)/(np.pi*m))
h[100]=1.0/4.0
plt.stem(m,h)
plt.show()