#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:19:44 2019

@author: lrgtomaszewski
"""

import matplotlib.pylab as plt


#Theory Results
#----------------------------------------
#Theory Results plot

X = (-0.20,-0.18,-0.16,-0.14,-0.12,-0.10,-0.08,-0.06,-0.04,-0.02,0.00,0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20)
Y = (0.6,0.53,0.47,0.41,0.34,0.27,0.21,0.14,0.08,0.02,0.00,0.02,0.08,0.14,0.21,0.27,0.34,0.41,0.47,0.53,0.60)

#----------------------------------------
#Actual Results plot

x = (-0.20,-0.18,-0.16,-0.14,-0.12,-0.10,-0.08,-0.06,-0.04,-0.02,0.00,0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20)
y = (-3.65,-3.60,-3.54,-3.45,-3.28,-2.89,-2.14,-1.00,-0.20,-0.29,0.00,-0.09,-0.48,-1.20,-2.06,-2.86,-3.31,-3.52,-3.94,-3.91,-3.86)

xerror = 0.001
yerror = 0.005

#----------------------------------------
plt.figure()
plt.plot(X,Y,'-b',label='Theoretical Results')
plt.plot(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.legend(loc='best')
plt.xlabel('Position (Metres)')
plt.ylabel('Magnetic Field (mT)')
plt.title('Air Solenoid $\pm20$ cm Position Vs Magnetic Field')
plt.savefig('Air_Solenoid_20_Position_Vs_Magnetic_Field.png')
plt.show()

print('Solution in mT')
print(Z)