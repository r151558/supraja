import cmath as cm
import numpy as np
import matplotlib. pyplot as plt

wc=np.pi/4
n=np.arange(-100,100,1)
h=(np.sin(wc*n)/(np.pi*n))
h[100]=1.0/4.0

def dtft(x):				#lpf
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(-np.pi,np.pi,N)
	for i in range(0,N):
		w=p[i]
		sum=0
		for k in range(0,n):
			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y
N=10000
p=np.linspace(-np.pi,np.pi,N)
t=dtft(h)



plt.plot(t)
plt.show()