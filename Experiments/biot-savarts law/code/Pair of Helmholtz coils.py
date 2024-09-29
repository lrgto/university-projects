#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:31:49 2019

@author: lrgtomaszewski
"""

import matplotlib.pylab as plt
#----------------------------------------
#Theory Results plot

X = (5.0,6.8,12.0,20.0)
Y = (4.11,3.18,1.05,0.24)
#----------------------------------------
#Actual Results plot

x = (5.0,6.8,12.0,20.0)
y = (5.67,4.75,2.73,1.19)

xerror = 0.05
yerror = 0.005

#----------------------------------------
plt.figure()
plt.plot(X,Y,'-b',label='Theoretical Results')
plt.plot(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.legend(loc='best')
plt.xlabel('Position (Metres)')
plt.ylabel('Magnetic Field (mT)')
plt.title('Pair of Helmholtz Coil Postion Vs Magnetic Field')
plt.savefig('Pair_Helmholtz_Coil_Position_Vs_Magnetic_Field.png')
plt.show()
