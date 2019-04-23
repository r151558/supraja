#buterworth LPF using BLT


import numpy as np
import matplotlib. pyplot as plt
import cmath as cm


wp=0.45*np.pi
ws=0.7*np.pi
ds=0.275
dp=0.9
T=1

def analog(wp,ws):
      Ap=(wp/2)
      As=(ws/2)
      return Ap,As

A=analog(wp,ws)
Ap=A[0]
print Ap
As=A[1]
print As



#order
def order(ds,dp,As,Ap):
       x1=((1.0/(ds**2))-1.0)
       x2=((1.0/(dp**2))-1.0)
       x=(x1/x2)
       y=(np.log(cm.sqrt(x))/np.log(As/Ap))
       return y

N=order(ds,dp,As,Ap)
n1=abs(N)
n2=np.ceil(n1)
print "order=", n2

#cutoff frequency

def    cutoff(As,ds,n2):
         t1=(1.0/(2.0*n2))
         t2=((ds**(-2))-1.0)
         t3=t2**t1
         y=As/t3
         return y

Ac=cutoff(As,ds,n2)
print "cutoff frequency",Ac


#transfer function

def tf(Ac,n2,T):
      k=((n2-1)/2)
      j=cm.sqrt(-1)
      bk=2*np.sin((((2*k)-1)*np.pi)/(2*n2))
      w=np.arange(0,np.pi,0.1)
      y2=1
      s=j*w
      z=np.exp(s*T)
      for k in range(1,3):					#k=1,2
             y1=((s**2)+(bk*Ac*s)+(Ac**2))
             y2=y2*y1
      y3=y2*(s+Ac)
      y=(Ac**n2)/y3
      return y

hs=tf(Ac,n2,T)
w=np.arange(0,np.pi,0.1)
plt.plot(w,abs(hs))
plt.show()
       





          

       






	

