import numpy as np
import cmath
def dft(x):
	y=[]
	j=cmath.sqrt(-1)
	N=len(x)
	for k in range (0,N):
		sum=0
		for n in range (0,N):
			sum=sum+(x[n]*np.exp(-j*2*np.pi*n*k/N))
		y=np.append(y,sum)
	print y
	return y
x=[1,2,3,4]
y=dft(x)
x1=[1,4,3,2]
y1=dft(x1)
