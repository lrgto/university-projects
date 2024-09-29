#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:05:35 2019

@author: lrgtomaszewski
"""

import matplotlib.pylab as plt
#----------------------------------------
#Theory Results plot

X = (0,30,60,90,120,150,180,210,240,270,300,330,360)
Y = (0.25,0.21,0.12,0.00,-0.12,-0.21,-0.25,-0.21,-0.12,0.00,0.12,0.21,0.25)

#----------------------------------------
#Actual Results plot

x = (0,30,60,90,120,150,180,210,240,270,300,330,360)
y = (0.15,0.18,0.11,-0.01,-0.14,-0.19,-0.20,-0.17,-0.15,0.01,0.14,0.16,0.15)

xerror = 5
yerror = 0.005

#----------------------------------------
plt.figure()
plt.plot(X,Y,'-b',label='Theoretical Results')
plt.plot(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.legend(loc='best')
plt.xlabel('Angle (Degress $\Theta$)')
plt.ylabel('Magnetic Field (mT)')
plt.title('Helmholtz Coil Tangential Angle Vs Magnetic Field')
plt.savefig('Helmholtz_Coil_Angle_2_Vs_Magnetic_Field.png')
plt.show()

print('Solution in mT')