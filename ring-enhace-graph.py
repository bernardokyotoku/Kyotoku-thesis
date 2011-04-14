#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('text',usetex=True)
mpl.rc('figure.subplot',left=0.15,bottom=0.18,right=0.95,top=0.95)
mpl.rc('text.latex',unicode=True)
mpl.rc('font',family='Latin Modern Roman',weight='light')
mpl.rc('legend',fontsize  = 10, borderpad=0.2,handletextpad=0.1)


plt.ion()
def drop(Lol,tau,t):
	pi = np.pi
	phi = 2*pi*Lol#length/wavelength
	t2 = t**2
	k2 = 1-t2
	return tau*k2**2/(1+tau**2*t2**2-2*tau*t2*np.cos(phi))

def gauss(Lol,dl,c):
	return 0.95*np.exp(-((Lol-c)/dl)**2)
	

lol = np.linspace(0.5,5.5,500)
tau = 0.99
t = 0.9
dl = 0.6
c = 1

fig1 = plt.figure(1,figsize=(3.2,2.4))
[plt.plot(lol,gauss(lol,dl,c),label='ch %d'%c) for c in range(1,6)] 
plt.plot(lol,drop(lol,tau,t),color='black',label='ring')
plt.xlim([0.5,5.5])
plt.legend(title='source')
plt.xlabel('$L/\\lambda_{eff}$')
plt.ylabel('Transmission')
plt.annotate('FSR',
	xy=(1.5,0.84),xycoords='data',
	va="top", ha="center", bbox=dict(boxstyle="round", fc="w"),
	arrowprops=dict(arrowstyle='->',
	connectionstyle='arc3')
	)
plt.annotate('',
	xy=(1,0.9),xycoords='data',
	xytext=(2,0.9),textcoords='data',
	va="top", ha="center", bbox=dict(boxstyle="round", fc="w"),
	arrowprops=dict(arrowstyle='<->',
	connectionstyle='arc3')
	)
fig1.savefig('ring-enhaced-sep.pdf')

fig2 = plt.figure(2,figsize=(3.2,2.4))
[plt.plot(lol,drop(lol,tau,t)*gauss(lol,dl,c),label='%d'%c)for c in range(1,6)] 
legend_font = mpl.font_manager.FontProperties(size=10,style='normal')
plt.legend(title='CH')
plt.xlim([0.5,5.5])
plt.ylim([0,1])
plt.xlabel('$L/\\lambda_{eff}$')
plt.ylabel('Transmission')
plt.annotate('crosstalk',
	xy=(2,0.05),xycoords='data',
	xytext=(2,0.4),textcoords='data',
	va="top", ha="center", bbox=dict(boxstyle="round", fc="w"),
	arrowprops=dict(arrowstyle='->',
	connectionstyle='arc3')
	)
plt.annotate('',
	xy=(2,0.85),xycoords='data',
	xytext=(2,0.4),textcoords='data',
	va="top", ha="center", bbox=dict(boxstyle="round", fc="w"),
	arrowprops=dict(arrowstyle='->',
	connectionstyle='arc3')
	)
fig2.savefig('ring-enhaced-tog.pdf')
raw_input()
