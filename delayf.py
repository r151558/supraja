import numpy as np
import cmath
j=cmath.sqrt(-1)
def dft(x):
	y=[]
	j=cmath.sqrt(-1)
	N=len(x)
	for k in range (0,N):
		sum=0
		for n in range (0,N):
			sum=sum+(x[n]*np.exp(-j*2*np.pi*n*k/N))
		y=np.append(y,sum)
	
	return y
x=[1,2,3,4]
y=dft(x)
print y
x2=[]
for k in range(0,4):
	x1=np.exp(j*2*np.pi*k/4)*x[k]
	x2=np.append(x2,x1)
y1=dft(x2)
print y1
	
