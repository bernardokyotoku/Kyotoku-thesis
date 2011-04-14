#!/usr/bin/env python
from numpy import *
from matplotlib.pyplot import *
import scientific_utils as su

T=range(1,11)
data = loadtxt('./T1-0.dat')
wavelength = data[:,0]
figure(10)
plot(wavelength,10*log10(data[:,1]))
figure(2)
mask =wavelength>1483
mask&=wavelength<1493
wavelength = wavelength[mask]
data = wavelength

for i in range(24,14,-1):
	for j in range(len(T)):
		filename = './T%d-%d.dat'%(T[j],i)
		print filename
		raw = loadtxt(filename)
		data = vstack((data,raw[mask,1]))
		wavelength = raw[mask,0]
		power = raw[mask,1]
		plot(wavelength,10*log10(power))
data = 40.5+10*log10(data)
data[0,:]=wavelength
savetxt('data1dB.dat',data.transpose(),fmt='%.8e')
input()
