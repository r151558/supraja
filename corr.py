import numpy as np
x=np.array(input("enter seq1:"))
h=np.array(input("enter seq2:"))
n1=len(x)
n2=len(h)
h1=[]
h1=np.zeros(n2)
for i in range (0,n2):
	h1[i]=h[n2-i-1]
print h1
n=n1+n2-1
y=np.zeros(n)
for p in  range(0,n):
	sum=0
	for q in  range(0,n1):
		if (p-q<n1 and p-q>=0):
			sum=sum+x[q]*h1[p-q]
		y[p]=sum
print y