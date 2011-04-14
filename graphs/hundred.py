#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
from matplotlib.colors import hsv_to_rgb
import scipy.signal as sgnl
rc('text',usetex=True)
dir = './data/2009-10-08/'
if not os.path.exists(dir+'data1dBt.dat'):
	data = np.loadtxt(dir+'data1dB.dat').transpose()
	np.savetxt(dir+'data1dBt.dat',data)
data = np.loadtxt(dir+'data1dBt.dat')
X = data[0]
n = len(X)
print n
resample_factor = 10 
X = X[np.arange(0,n,resample_factor)]
fig = plt.figure(1,figsize = (7,3))
ax = fig.add_axes([0.1,0.15,0.85,0.8])
for i in range(100):
	Y = data[i+1,np.arange(0,n,resample_factor)]
	plt.plot(X,Y,color=hsv_to_rgb(np.array([[[0.8-i*0.008,1,1]]]))[0,0])
#plt.plot(sgnl.resample(data[1],resample_factor))
#plt.show()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Transmission (dB)')
plt.xlim([1483,1493])
plt.ylim([-40,-15])
plt.savefig('hundred.pdf')
