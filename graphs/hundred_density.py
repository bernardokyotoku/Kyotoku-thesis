#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
from matplotlib.colors import hsv_to_rgb
import scipy.signal as sgnl
rc('text',usetex=True)
dire = './data/2009-10-08/'
if not os.path.exists(dire+'data1dBt.dat'):
	data = np.loadtxt(dire+'data1dB.dat').transpose()
	np.savetxt(dire+'data1dBt.dat',data)
data = np.loadtxt(dire+'data1dBt.dat')
X = data[0]
n = len(X)
resample_factor = 10 
X = X[np.arange(0,n,resample_factor)]
fig = plt.figure(1,figsize = (7,2.5))
image = np.nan_to_num(data[1:,np.arange(0,n,resample_factor)])
mask = np.logical_or(image<-40,image==0)
image = image-40*mask-image*mask
cax = plt.imshow(image,aspect=5.0/3,cmap='Reds')
plt.xticks(range(0,600,100),[str(int(round(i))) for i in np.linspace(X[0],X[-1],6)])
#plt.adjust(top=0.9)
colorbar = plt.colorbar(cax, orientation='vertical')
colorbar.set_label('Transmission (dB)')
#plt.plot(sgnl.resample(data[1],resample_factor))
#plt.show()
#plt.xlim([1483,1493])
#plt.ylim([-40,-15])
plt.ylabel('Channel')
plt.xlabel('Wavelength (nm)')
plt.savefig('hundred_density.pdf',bbox_inches='tight')
