#!/usr/bin/env python

import numpy as np
from numpy import pi
import matplotlib
import matplotlib.pyplot as plt

d = 4
neff = 2.975 
leff = 1.5/neff
m = -10

outAngle = lambda inAngle: np.arcsin(m*leff/d + np.sin(inAngle))

thetaIn = np.linspace(0,pi/2,100)
thetaOut = outAngle(thetaIn)

plt.plot(thetaIn,thetaOut)
plt.gcf().set_size_inches([3.2,2.4])
plt.xlabel('$\\theta_0$ (rad)')
plt.ylabel('$\\theta$ (rad)')
plt.xticks(np.linspace(0,pi/2,7),['$0$']+['$\\frac{%d}{12}\pi$'%i for i in range(1,7)])
plt.yticks(np.linspace(0,-pi/2,7),['$0$']+['$\\frac{%d}{12}\pi$'%i for i in range(1,7)])
plt.subplots_adjust(bottom=0.2)
plt.savefig('outAngleXinAngle.pdf')
plt.show()
