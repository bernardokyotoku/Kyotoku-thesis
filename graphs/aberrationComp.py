#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
import os
import scipy.signal as sgnl
#rc('text',usetex=True)
print matplotlib.matplotlib_fname()
dir = './data/'
data = np.loadtxt(dir+'aberrationComp.dat')
X = data[0]*10**6
stigmatic = data[1]*10**9
uniform = data[2]*10**9
n = len(X)
fig = plt.figure(1,figsize = (3.2,2.4))
#fig.add_subplot(111)
ax = fig.add_axes([0.15,0.15,0.8,0.8])
plt.plot(X,uniform,label='uniform')
plt.plot(X,stigmatic)
plt.xlabel('Wavelength ($\mu$m)')
plt.ylabel('FWHM (nm)')
ax.annotate('Uniform',xy=(1.60,1.3),xytext=(1.59,1.1), arrowprops=dict(facecolor='black', shrink=0.01))
ax.annotate('Stigmatic',xytext=(1.6,0.5),xy=(1.61,0.7), arrowprops=dict(facecolor='black', shrink=0.01))
#plt.legend(['Uniform Grating','Stigmatic Corrected'])
#plt.show()
#plt.xlim([1483,1493])
#plt.ylim([-40,-15])
plt.savefig('aberrationComp.pdf')
