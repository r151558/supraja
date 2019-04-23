import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import numpy as np
fs,data=wav.read('my.wav')
wav.write('low_my.wav',4*fs,data)
wav.write('high_my.wav',fs/4,data)
print (fs,data,len(data))
plt.plot(data)
plt.show()

