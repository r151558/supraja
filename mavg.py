import matplotlib.pyplot as plt
import numpy as np
Fs=100
f=9
sample=100
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
b=np.random.rand(y.shape[0])
z=y+b
p=input("enter the order of the system:")
l=len(x)
sum=0
for k in range(l):
	m=0
	for i in range(0,p-1):
		m=m+z[k-i]
plt.subplot(411)
plt.plot(x,y)
plt.subplot(412)
plt.plot(b)
plt.subplot(413)
plt.plot(x,z)
plt.subplot(414)
plt.plot(m)
plt.show()