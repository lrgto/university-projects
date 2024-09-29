# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pylab as plt

#----------------------------------------
#Theory Results plot

X = (0.10,0.15,0.20,0.25,0.30,0.35,0.40)
Y = (0.28,0.44,0.60,0.75,0.90,1.05,1.20)

#----------------------------------------
#Actual Results plot

x = (0.10,0.15,0.20,0.25,0.30,0.35,0.40)
y = (-5.15,-3.88,-3.20,-2.48,-2.15,-1.85,-1.55)

xerror = 0.001
yerror = 0.005

#----------------------------------------
plt.figure()
plt.plot(X,Y,'-b',label='Theoretical Results')
plt.plot(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.xlabel('Positon (Metres)')
plt.ylabel('Magnetic Field (mT)')
plt.legend(loc='upper left')
plt.title('Air Solenoid +5cm Position Vs Magnetic Field')
plt.savefig('Air_Solenoid_Position_Vs_Magnetic_Field.png')
plt.show()

print('Solution in mT')
print(Z)