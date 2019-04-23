import numpy as np
x=np.array(input("enter first seq:"))
h=np.array(input("enter second seq:"))
n1=len(x)
n2=len(h)
n=n1+n2-1
y=np.zeros(n)
for p in  range(0,n):
	sum=0
	for q in  range(0,n1):
		if (p-q<n1 and p-q>=0):
			sum=sum+x[q]*h[p-q]
		y[p]=sum
print y
