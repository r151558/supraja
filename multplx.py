import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,d8k=wav.read('suppu3.wav')
print(fs,len(d8k))
print(d8k)
fs1,d9k=wav.read('suppu1.wav')
print(fs1,len(d9k))
print(d9k)
fs2,d1k=wav.read('supp4.slow')
print(fs2,len(d1k))
print(d1k)
t=np.arange(0,len(d8k)/fs,1.0/fs)
t1=np.arange(0,len(d9k)/fs1,1.0/fs1)
t2=np.arange(0,len(d1k)/fs2,1.0/fs2)

plt.subplot(3,1,1)
plt.plot(d8k)

plt.subplot(3,1,2)
plt.plot(d9k)

plt.subplot(3,1,3)
plt.plot(d1k)

plt.show()
