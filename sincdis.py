import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-20,20,0.5)
x1=np.sinc(t)

plt.stem(t,x1,'g')
plt.title('sinc function waveform')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

