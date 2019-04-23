import matplotlib.pyplot as plt
import numpy as np
f1=100
fs1=3000
y1=np.arange(0,100,1)
x1=np.cos(2*np.pi/2*y1*f1/fs1)
plt.subplot(311)
plt.plot(y1,x1)
f2=200
fs2=2500
y2=np.arange(0,100,1)
x2=np.cos(2*np.pi*y2*f2/fs2)
plt.subplot(312)
plt.plot(y2,x2)
x=x1+x2
plt.subplot(313)
plt.plot(y1,x)
plt.xlabel('-------------->n')
plt.ylabel('-------------->voltage')
plt.show()