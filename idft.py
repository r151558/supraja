import numpy as np
import cmath
import matplotlib.pyplot as plt
j=cmath.sqrt(-1)
x=[1.0,-j/3.0,1.0/3.0,j/3.0]
M=input("enter the period of dft:")
m=len(x)
print m
i=m-1
j=cmath.sqrt(-1)
y=[]
for n in range(0,M):
	sum=0
	for k in range(0,M):
		sum=sum+x[k]*np.exp(j*2*np.pi*n*k/M)
	z=sum/M
	y=np.append(y,z)
print( y)
y1=np.abs(y)
plt.stem(y1)
plt.show()
y2=np.angle(y)
plt.stem(y2)
plt.show()