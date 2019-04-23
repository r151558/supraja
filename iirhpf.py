import numpy as np
import matplotlib.pyplot as plt
import math
import cmath as cm
del_1=0.6
del_s=0.1
w_p=0.7*np.pi
w_s=0.35*np.pi
t=0.1
j=cm.sqrt(-1)
wo_p=(2/t)*np.tan(w_p/2)
wo_s=(2/t)*np.tan(w_s/2)
d_s=del_s**-2
d_p=del_1**-2
x=(d_s-1)/(d_p-1)
print(x)
sq=np.sqrt(x)
wo_s1=wo_p/wo_s
wo_p1=wo_p/wo_p
dq=wo_s1/wo_p1
print('sq',sq)
print('dq',dq)
N_0=(math.log(sq,10))/(math.log(dq,10))
N=math.ceil(N_0)
print('N',N)
p=1/(2*N)
w_c=wo_s1/((d_s-1)**p)
print('w_c',w_c)
w=np.linspace(0,np.pi,1000)
z=np.exp(j*w)
print('z',z)
s=2/t*((1-(z**-1))/(1+(z**-1)))
s1=wo_p/s
print('s1',s1)
#k=np.arange(0,N/2)
k=1
#print(k)
bk=2*np.sin(2*k-1)*np.pi/(2*N)
n=((w_c)**N)
y=((s1**2)+bk*w_c*s1+(w_c**2))
H_S1=n/y
print('H_S1',H_S1)
plt.plot(w,abs(H_S1))
plt.show()








