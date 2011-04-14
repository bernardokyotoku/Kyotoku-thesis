#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.signal as sgnl

rc('text',usetex=True)
plt.ion()
fig = plt.figure(1,figsize=[7,2])
ax = fig.add_axes([0.1,0.21,0.85,0.7])
x = np.linspace(0,9,10)
plt.bar(x,np.exp(-0.3*x),width=0.05)
plt.xlabel('delay ($n_{eff}L/\\lambda$)')
plt.ylabel('$E_1\\kappa_a\\kappa_b\\sqrt{\\tau}$')
plt.savefig('exp_decay.pdf')
raw_input()
