# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 

import matplotlib.pylab as plt

#Theory Results

r = (-0.030,-0.025,-0.020,-0.015,-0.010,-0.005,0.00,0.005,0.010,0.015,0.020,0.025,0.030)
Z = (0.14,0.21,0.0,0.2,0.19,0.17,0.11,0.1,0.14,0.13,0.11,0.1,0.08)


#----------------------------------------
#Theory Results plot

X = (r)
Y = (Z)

#----------------------------------------
#Actual Results plot

x = (-0.030,-0.025,-0.020,-0.015,-0.010,-0.005,0.00,0.005,0.010,0.015,0.020,0.025,0.030)
y = (0.09,0.11,0.13,0.10,0.08,0.03,0.00,-0.11,-0.22,-0.16,-0.03,0.01,0.09)

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
plt.title('Straight Conductor $\pm3$ cm Position Vs Magnetic Field')
plt.savefig('Straight_Conductor_Position_Vs_Magnetic_Field.png')
plt.show()

print('Solution in mT')
print(Z)