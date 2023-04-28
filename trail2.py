# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:03:10 2023

@author: acer
"""

import numpy as np
import matplotlib.pyplot as plt

# read data from file
rawinput = np.genfromtxt('data0.csv', delimiter=' ')

# derive the distribution of values by binning them into 20 bins
# ohist contains numbers of entries in each bin, oedge contains bin boundaries
ohist, oedge = np.histogram(rawinput, bins=20)

# calculate bin centre locations and bin widths
xdst = 0.5*(oedge[1:]+oedge[:-1])
wdst = oedge[1:]-oedge[:-1]

# normalise the distribution
# ydist is a discrete PDF
ydst = ohist/np.sum(ohist)

# cumulative distribution
cdst = np.cumsum(ydst)

plt.figure(figsize=(8,5))

# Plot the PDF
plt.bar(xdst, ydst, width=0.9*wdst)

plt.xlabel('Weight', fontsize=15)
plt.ylabel('frequency', fontsize=15)

plt.title('Distribution of weight of Newborns', fontsize=20)
# Mean value
xmean = np.sum(xdst*ydst)
# and plot it
text = ''' Mean value: {}'''.format(np.round(xmean, 2))
plt.text(x=xmean, y=max(ydst), s=text, fontsize=12, c='red')
plt.axvline(xmean, color='y', linestyle=':', label='mean')



# find value X such that 0.75 of the distribution corresponds to values>Xvalue
indx = np.argmin(np.abs(cdst-0.25))
xhigh = oedge[indx]
plt.bar(xdst[indx:], ydst[indx:], width=0.9*wdst[indx:], color='green')
plt.axvline(xhigh, ymax=0.5, color='b', linestyle=':', label='X Value')
text = ''' X value: {}'''.format(np.round(xhigh, 2))
plt.text(x=2.5, y=0.07, s=text, fontsize=12, c='red')

plt.legend()