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
h=[0,1,3,4]
X=dft(x)
H=dft(h)
x1=[]
for n in range(0,4):
	s=x[n]*h[n]
	x1=np.append(x1,s)
print x1
X1=dft(x1)

print X1
Y=[]
for n in range(0,7):
	sum=0
	for m in range(0,4):
		if(n-m>=0 and n-m<4):
			sum=(sum+X[m]*H[n-m])
	s=sum/4
	Y=np.append(Y,s)

z1=[]
for i in range(4,7):
	z=Y[i]+Y[i-4]
	z1=np.append(z1,z)
w=Y[3]
z1=np.append(z1,w)
print z1

	
