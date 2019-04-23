import numpy as np
import cmath
import matplotlib.pyplot as plt
j=cmath.sqrt(-1)
x=[1.0/3.0,1.0/3.0,1.0/3.0,0]
y=[]
y=np.zeros(10000)
w=np.linspace(0,2*np.pi,10000)
for i in range(0,10000):
	sum=0
	for n in range(0,3):
		sum=sum+x[n]*(np.exp(-j*w[i]*n))
	y[i]=sum
	y=np.append(y,sum)
print y
m=np.abs(y)
plt.subplot(2,1,1)
plt.plot (m)
a=np.angle(y)
plt.subplot(2,1,2)
plt.plot(a)
plt.show	()
