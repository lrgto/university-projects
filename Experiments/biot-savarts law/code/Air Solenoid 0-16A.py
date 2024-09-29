# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pylab as plt
import numpy as np
import math

#Theory Results

I = np.arange(0,18,2)
L = 0.15
N = 30
px = 0
R = 0.042

a = (px + (L/2))/(math.sqrt(((px+L/2)**2)+R**2))

b = (px - (L/2))/(math.sqrt(((px-L/2)**2)+R**2))

l = a - b

n = 100

u = 0.00000126

B = u * I * n * l

Z = B * 1000

#----------------------------------------
#Theory Results plot

X = (I)
Y = (Z)

#----------------------------------------
#Actual Results plot

x = (0,2,4,6,8,10,12,14,16)
y = (0.00,-0.48,-0.98,-1.45,-1.92,-2.40,-2.92,-3.40,-3.86)

xerror = 0.1
yerror = 0.005

#----------------------------------------
plt.figure()
plt.plot(X,Y,'-b',label='Theoretical Results')
plt.plot(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.xlabel('Current (Amps)')
plt.ylabel('Magnetic Field (mT)')
plt.legend(loc='upper left')
plt.title('Air Solenoid 0-16A Current Vs Magnetic Field')
plt.savefig('Air_Solenoid_0-16A_Graph.png')
plt.show()

print('Solution in mT')
print(Z)