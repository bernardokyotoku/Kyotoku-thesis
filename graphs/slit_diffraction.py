#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
#from matplotlib.rc as rc

slit_widths = [4,2,1 ]
wavelength = 1
k=2*np.pi/wavelength
def f(a,x,y):
	r = np.sqrt(x**2+y**2)
	p = x/r
	return (1/r**1)*(np.sin(a*p)/(p*a))**2

xpoints = 400
ypoints = 300
width = 1000
height = 1000
X,Y=np.meshgrid(np.linspace(-width/2,width/2,xpoints),
		np.linspace(height,0.0,ypoints))

#ploting

for slit_width in slit_widths:
	image = f(k*slit_width,X,Y)
	s=0.01
	m=0.05
	cdict = {'red': ((0.0, 1.0, 1.0),
			 (s, 1.0, 1.0),
			 (m, 0.4, 0.4),
			 (1.0, 0.4, 0.4)),
		 'green': ((0.0, 1.0, 1.0),
			   (s, 0.0, 0.0),
			   (m, 0.0, 0.0),
			   (1.0, 0.0, 0.0)),
		 'blue': ((0.0, 1.0, 1.0),
			  (s, 0.0, 0.0),
			  (m, 0.0, 0.0),
			  (1.0, 0.0, 0.0))}
	my_cmap = colors.LinearSegmentedColormap('my_colormap',cdict,2**16)
	fig = plt.figure(1,figsize=[4,3])
	ax = fig.add_axes([0,0,1,1])
	ax.cla()
	plt.imshow(image,cmap=my_cmap)

	#plt.show()
	#plt.ylim([-0.1,1.1])
	plt.axis("off")
	plt.savefig('slit_width-%d.png'%slit_width)

	fig2 = plt.figure(2)
	fig2.clear()
	plt.plot(f(k*slit_width,X[0],Y[0]))
	#plt.axis('off')
	plt.ylim([-0.0001,0.0011])
	plt.savefig('slit_diff_graph-%d.pdf'%slit_width)
