#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
from matplotlib import rc
rc('text', usetex=True)
plt.close('all')
number_points = 500
F = lambda N,x : (np.sin(N*x)/np.sin(x))**2
FN = lambda N,x: F(N,x)/max(F(N,x))
sinc =lambda x: (np.sin(x)/x)**2
fig = plt.figure(figsize=(6,8), dpi=None, facecolor=None, edgecolor=None, linewidth=1.0, frameon=True, subplotpars=None)
axis1 = plt.subplot(311)
axis1.plot(np.linspace(0,12.5,number_points),FN(6,np.linspace(-0.1,np.pi*12.5,number_points)))
axis1.set_xlabel('p')
#axis1.spines['top'].set_alpha(None)
axis1.spines['top'].set_color(color.ColorConverter().to_rgb('w'))
axis1.spines['right'].set_color(color.ColorConverter().to_rgb('w'))
axis1.tick_params(top=False)
axis1.tick_params(right=False)
#axis1.axis()[0].tick_params(top=False)
plt.xticks(np.linspace(0,12.5,26),("$O$",'',"${\lambda/d}$","","${2\lambda/d}$")+
			tuple(['']*21))
plt.yticks([0,0.5,1,1.1],("","(a)","1",""))
axis2 = plt.subplot(312)
axis2.plot(np.linspace(0,3*np.pi,number_points),sinc(np.linspace(-0.1,3*np.pi,number_points)))
plt.xticks(np.linspace(0,np.pi*3,4),("$O$","$\lambda/s$","$2\lambda/s$","$3\lambda/s$"))
plt.yticks([0,0.5,1,1.1],("","(b)","1",""))
axis2.spines['top'].set_color(color.ColorConverter().to_rgb('w'))
axis2.spines['right'].set_color(color.ColorConverter().to_rgb('w'))
axis2.tick_params(top=False)
axis2.tick_params(right=False)

axis3 = plt.subplot(313)
axis3.plot(np.linspace(0,3*np.pi,number_points),FN(6,np.linspace(-0.1,np.pi*12.5,number_points))*sinc(np.linspace(-0.1,3*np.pi,number_points)))
axis3.plot(np.linspace(0,3*np.pi,number_points),sinc(np.linspace(-0.1,3*np.pi,number_points)),color='r')
plt.xticks(np.linspace(0,np.pi*3,4),("$O$","$\lambda/s$","$2\lambda/s$","$3\lambda/s$"))
plt.yticks([0,0.5,1,1.1],("","(c)","1",""))
axis3.spines['top'].set_color(color.ColorConverter().to_rgb('w'))
axis3.spines['right'].set_color(color.ColorConverter().to_rgb('w'))
axis3.tick_params(top=False)
axis3.tick_params(right=False)
plt.savefig("diffraction grating basic.eps")

