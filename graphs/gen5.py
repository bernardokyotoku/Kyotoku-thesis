#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import shutil
import os
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']))
rc('text', usetex=True)
rc('font',family='serif')
dir = "./data/2008-11-15/S4/"
if not os.path.exists(dir):
	os.makedirs(dir)
	original_dir = "/Users/bernardo/data/2008-11-15/S4/"
	for file in os.listdir(original_dir):
		shutil.copy(original_dir+file,dir)
#resampling
resampling_factor = 30
if not os.path.exists(dir+"data-1-%d.dat"%resampling_factor):
	for i in range(21):
		[X,Y] = np.loadtxt(dir+"ch%d.dat"%(i+1)).transpose()
		points = len(Y)/resampling_factor
		Y = sig.resample(Y,points)
		X = sig.resample(X,points)
		np.savetxt(dir+"data-%d-%d.dat"%(i,resampling_factor),np.vstack([X,Y]))	

[X,Y] = np.loadtxt(dir+"refTE.dat").transpose()
points = len(Y)/resampling_factor
Y = sig.resample(Y,points)
X = sig.resample(X,points)
np.savetxt(dir+"refTE-%d.dat"%(resampling_factor),np.vstack([X,Y]))	
refLevel = 10*np.log10(np.mean(Y))
#ploting
fig = plt.figure(figsize=[7,4])
ax = plt.subplot(111)
for i in range(21):
	[X,Y] = np.loadtxt(dir+"data-%d-%d.dat"%(i,resampling_factor))
	Y = 10*np.log10(Y)-refLevel
	ax.plot(X,Y)
plt.xlabel(r'Wavelength (nm)')
plt.ylabel(r'Transmission (dB)')
plt.xlim([1485,1525])
plt.ylim([-30,-5])
#plt.show()
plt.savefig("gen5.eps")
plt.savefig("gen5.pdf")
