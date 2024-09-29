#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:31:49 2019

@author: lrgtomaszewski
"""
import matplotlib.pylab as plt
#----------------------------------------
#Theory Results plot

X = (-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10)
Y = (0.78,0.96,1.19,1.49,1.86,2.31,2.84,3.40,3.93,4.32,4.46,4.32,3.93,3.40,2.84,2.31,1.86,1.49,1.19,0.96,0.78)

#----------------------------------------
#Actual Results plot

x = (-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10)
y = (0.85,1.01,1.25,1.53,1.90,2.36,2.89,3.55,4.06,4.50,4.73,4.67,4.29,3.77,3.16,2.62,2.12,1.70,1.37,1.13,0.92)

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
plt.title('Helmholtz Coil $\pm10$ cm Postion Vs Magnetic Field')
plt.savefig('Helmholtz_Coil_Position_Vs_Magnetic_Field.png')
plt.show()
