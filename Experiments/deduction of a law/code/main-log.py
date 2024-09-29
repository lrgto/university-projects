import matplotlib.pylab as plt
import numpy as np
import os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

XArea, YArea = np.genfromtxt(dir+'/source/Main(Log) Results.csv', delimiter = ',',usecols=[0,1], unpack = True)
XArea = np.sort(XArea)
YArea = np.sort(YArea)

XDensity, YDensity = np.genfromtxt(dir+'/source/Main(Log) Results.csv', delimiter = ',',usecols=[2,3], unpack = True)
XDensity = np.sort(XDensity)
YDensity = np.sort(YDensity)

XThickness, YThickness = np.genfromtxt(dir+'/source/Main(Log) Results.csv', delimiter = ',',usecols=[4,5], unpack = True)
XThickness = np.sort(XThickness)
YThickness = np.sort(YThickness)

XSideLength, YSideLength = np.genfromtxt(dir+'/source/Main(Log) Results.csv', delimiter = ',',usecols=[6,7], unpack = True)
XSideLength = np.sort(XSideLength)
YSideLength = np.sort(YSideLength)

plt.figure()
plt.plot(XArea, YArea,)
plt.xlabel('Log of Area (mm^2)')
plt.ylabel('Log of Period (s)')
plt.title('Area Vs Period of Oscillation')
plt.savefig(dir+'/results/Log_AreaVsPeriod.png')
plt.close()

plt.figure()
plt.plot(XDensity, YDensity,)
plt.xlabel('Log of Density (g/mm^3)')
plt.ylabel('Log of Period (s)')
plt.title('Density Vs Period of Oscillation')
plt.savefig(dir+'/results/Log_DensityVsPeriod.png')
plt.close()

plt.figure()
plt.plot(XThickness, YThickness,)
plt.xlabel('Log of Thickness (mm)')
plt.ylabel('Log of Period (s)')
plt.title('Thickenss Vs Period of Oscillation')
plt.savefig(dir+'/results/Log_ThicknessVsPeriod.png')
plt.close()

plt.figure()
plt.plot(XSideLength, YSideLength,)
plt.xlabel('Log of Side Length (mm)')
plt.ylabel('Log of Period (s)')
plt.title('Side Length Vs Period of Oscillation')
plt.savefig(dir+'/results/Log_Side_LengthVsPeriod.png')
plt.close()