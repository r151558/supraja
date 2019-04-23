import numpy as np
from matplotlib import pyplot as plt
f=20
fs=400
x=np.arange(0,100,0.1)
y=np.sin((2*np.pi*x*20)/400)
n1=np.random.rand(y.shape[0])
n=y+n1
ry=-y
rn1=np.random.rand(ry.shape[0])
rn=ry+rn1
h=[1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3,1.0/3]
s=np.convolve(rn,h)
plt.subplot(6,1,1)
plt.plot(x,y)
plt.subplot(6,1,2)
plt.plot(ry)
plt.subplot(6,1,3)
plt.plot(n1)
plt.subplot(6,1,4)
plt.plot(rn1)
plt.subplot(6,1,5)
plt.plot(rn)
plt.plot(6,1,6)
plt.show()