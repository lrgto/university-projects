import os, math, numpy as np, matplotlib.pyplot as plt, pandas as pd

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#----------------------------------------------------------------------------------------------
# 40mm 0-16A
I = np.arange(0,18,2) # Current
R = 0.02 # Radius
X = 0
B = 0.0000001 * (I * ((2 * math.pi * R**2)/((R**2 + X**2)**(1.5))))
Z1 = B * 1000
X,Y = (I),(Z1)

x = (0,2,4,6,8,10,12,14,16)
y = (0.00,0.06,0.10,0.15,0.17,0.25,0.27,0.31,0.37)
xerr, yerr = 0.1, 0.005

plt.figure()
plt.plot(X,Y,label='Theoretical Results')
plt.plot(x,y,'r',label='Actual Results')
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='r', ecolor='red', capsize=1)
plt.xlabel('Current (Amps)', labelpad=10); plt.ylabel('Magnetic Field (mT)', labelpad=10); plt.legend(loc='best')
plt.title('40mm Conductor Loop 0-16A Current Vs Magnetic Field', pad=10, fontsize=11)
plt.savefig(dir+'/Image Results/CL_40mm_0-16A_CurrentVsMagneticField.png', dpi=500, bbox_inches="tight")
plt.close()

#----------------------------------------------------------------------------------------------
# 40mm 16A ±10cm
I = 16
R = 0.02
X = np.arange(-0.10,0.11,0.01)
B = 0.0000001 * (I * ((2 * math.pi * R**2)/((R**2 + X**2)**(1.5))))
Z = B * 1000
X,Y = (X),(Z)

x = (-0.10,-0.09,-0.08,-0.07,-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10)
y = (0.00,0.00,0.01,0.01,0.01,0.02,0.02,0.05,0.10,0.19,0.34,0.54,0.34,0.16,0.07,0.03,0.02,0.01,0.00,0.00,0.00)
xerr = 0.001
yerr = 0.005

plt.figure()
plt.plot(X,Y,label='Theoretical Results')
plt.plot(x,y,'r',label='Actual Results')
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='r', ecolor='red', capsize=1)
plt.xlabel('Position (Metres)', labelpad=10); plt.ylabel('Magnetic Field (mT)', labelpad=10); plt.legend(loc='best')
plt.title('40mm Conductor Loop $\pm10$cm Position Vs Magnetic Field', pad=10, fontsize=11)
plt.savefig(dir+'/Image Results/CL_40mm_16A_PositionVsMagneticField.png', dpi=500, bbox_inches="tight")
plt.close()
#----------------------------------------------------------------------------------------------
# 80mm 16A ±10cm
I = 16
R = 0.04
X = np.arange(-0.10,0.11,0.01)
B = 0.0000001 * (I * ((2 * math.pi * R**2)/((R**2 + X**2)**(1.5))))
Z = B * 1000
X,Y = (X),(Z)

x = (-0.10,-0.09,-0.08,-0.07,-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10)
y = (-0.01,-0.01,0.00,0.01,0.01,0.02,0.05,0.10,0.12,0.18,0.20,0.25,0.20,0.16,0.10,0.06,0.02,0.02,0.02,0.00,0.00)

xerr = 0.001
yerr = 0.005

plt.figure()
plt.plot(X,Y,label='Theoretical Results')
plt.plot(x,y,'r',label='Actual Results')
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='r', ecolor='red', capsize=1)
plt.xlabel('Position (Metres)', labelpad=10); plt.ylabel('Magnetic Field (mT)', labelpad=10); plt.legend(loc='best')
plt.title('80mm Conductor Loop $\pm10$cm Position Vs Magnetic Field', pad=10, fontsize=11)
plt.savefig(dir+'/Image Results/CL_80mm_16A_PositionVsMagneticField.png', dpi=500, bbox_inches="tight")
plt.close()
#----------------------------------------------------------------------------------------------
# 120mm 16A ±10cm
I = 16
R = 0.06 
X = np.arange(-0.10,0.11,0.01)
B = 0.0000001 * (I * ((2 * math.pi * R**2)/((R**2 + X**2)**(1.5))))
Z = B * 1000
X,Y = (X),(Z)

x = (-0.10,-0.09,-0.08,-0.07,-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10)
y = (0.00,0.00,0.00,0.01,0.01,0.04,0.05,0.09,0.10,0.12,0.15,0.14,0.13,0.11,0.08,0.08,0.06,0.03,0.01,0.00,-0.01)

xerr = 0.001
yerr = 0.005

plt.figure()
plt.plot(X,Y,label='Theoretical Results')
plt.plot(x,y,'r',label='Actual Results')
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='r', ecolor='red', capsize=1)
plt.xlabel('Position (Metres)', labelpad=10); plt.ylabel('Magnetic Field (mT)', labelpad=10); plt.legend(loc='best')
plt.title('120mm Conductor Loop $\pm10$cm Position Vs Magnetic Field', pad=10, fontsize=11)
plt.savefig(dir+'/Image Results/CL_120mm_16A_PositionVsMagneticField.png', dpi=500, bbox_inches="tight")
plt.close()
#----------------------------------------------------------------------------------------------
# 40,80,120mm 16A ±10cm Comparison
X = (-0.1,-0.09,-0.08,-0.07,-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10)
Y40 = (0.00,0.00,0.01,0.01,0.01,0.02,0.02,0.05,0.10,0.19,0.34,0.54,0.34,0.16,0.07,0.03,0.02,0.01,0.00,0.00,0.00)
Y80 = (-0.01,-0.01,0.00,0.01,0.01,0.02,0.05,0.10,0.12,0.18,0.20,0.25,0.20,0.16,0.10,0.06,0.02,0.02,0.02,0.00,0.00)
Y120 = (0.00,0.00,0.00,0.01,0.01,0.04,0.05,0.09,0.10,0.12,0.15,0.14,0.13,0.11,0.08,0.08,0.06,0.03,0.01,0.00,-0.01)

xerr = 0.001
yerr = 0.005

plt.figure()
plt.plot(X,Y120,'-b',label='120mm Conductor Loop')
plt.errorbar(X, Y120, xerr=xerr, yerr=yerr, fmt='-b', ecolor='blue', capsize=1)
plt.plot(X,Y80,'-r',label='80mm Conductor Loop')
plt.errorbar(X, Y80, xerr=xerr, yerr=yerr, fmt='-r', ecolor='red', capsize=1)
plt.plot(X,Y40,'-g',label='40mm Conductor Loop')
plt.errorbar(X, Y40, xerr=xerr, yerr=yerr, fmt='-g', ecolor='green', capsize=1)
plt.xlabel('Position (Metres)', labelpad=10); plt.ylabel('Magnetic Field (mT)', labelpad=10); plt.legend(loc='best')
plt.title('Comparison of 40, 80, 120mm Conductor Loop $\pm10$cm Position Vs Magnetic Field', pad=10, fontsize=11)
plt.savefig(dir+'/Image Results/CL_40-80-120mm_16A_PositionVsMagneticField.png', dpi=500, bbox_inches="tight")
plt.close()