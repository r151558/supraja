import numpy as np
import cmath
import matplotlib.pyplot as plt
x=np.array(input("enter irst sequence:"))
M=input("enter the period of dft:")
m=len(x)
print m
i=m-1
j=cmath.sqrt(-1)
y=[]
for k in range(0,M):
	sum=0
	for n in range(0,M):
		sum=sum+x[n]*np.exp(-j*2*np.pi*n*k/M)
	y=np.append(y,sum)
print( y)
y1=np.abs(y)
plt.stem(y1)
plt.show()
y2=np.angle(y)
plt.stem(y2)
plt.show()