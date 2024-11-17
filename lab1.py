import matplotlib.pyplot as plt
from scipy.fftpack import rfft,fftfreq, irfft
import numpy as np
iterator1 = 0
iterator2 = 1
X, Y = [], []
xline = 0
for yline in open('data.dat', 'r'):
 #values = [float(s) for s in yline.split('\n')]
  X.append(xline)
  Y.append(float(yline.replace('\n','')))
  xline += 1
yf = rfft(Y)
yf = np.abs(yf)
half_x = X[:int(xline/2)]
while(iterator1 < 180):
 if (iterator2%3==0):
  iterator1 +=1
  iterator2 += 1
  continue
 yf[iterator1] = 0
 iterator1 += 1
 iterator2 += 1
new_sig = irfft(yf)
plt.plot(X,new_sig)
plt.show()