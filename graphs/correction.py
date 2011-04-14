#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

dir = './data/2010-09-28/'
data = np.loadtxt(dir+'data.dat')

X = data[0]*10**6
Y = data[1:]

plt.plot(X,Y[0])

plt.savefig('one-stigmatic.png')
