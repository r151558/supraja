import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,d8k=wav.read('voice.wav')
print(fs,len(d8k))
print(d8k)
t=np.arange(0,len(d8k)/fs,1.0/fs)
plt.plot(d8k)
plt.show()
wav.write('supp3.wav',2*fs,d8k)
