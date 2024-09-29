#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:31:46 2019

@author: lrgtomaszewski
"""

import matplotlib.pylab as plt

#Theory Results


#----------------------------------------
#Theory Results plot

X = (0,30,60,90,120,150,180,210,240,270,300,330,360)
Y = (0.17,0.14,0.08,0.00,-0.08,-0.14,-0.17,-0.14,-0.08,0.00,0.08,0.14,0.17)

#----------------------------------------
#Actual Results plot

x = (0,30,60,90,120,150,180,210,240,270,300,330,360)
y = (0.15,0.12,0.11,0.00,-0.05,-0.05,-0.08,-0.10,-0.08,-0.06,0.00,0.09,0.13)

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
plt.title('Helmholtz Coil Axial Angle Vs Magnetic Field')
plt.savefig('Helmholtz_Coil_Angle_1_Vs_Magnetic_Field.png')
plt.show()

print('Solution in mT')