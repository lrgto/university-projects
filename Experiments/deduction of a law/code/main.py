import matplotlib.pyplot as plt, numpy as np, os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

XArea, YArea = np.genfromtxt(dir+'/source/Main Results.csv', delimiter = ',',usecols=[0,1], unpack = True)

XDensity, YDensity = np.genfromtxt(dir+'/source/Main Results.csv', delimiter = ',',usecols=[2,3], unpack = True)

XThickness, YThickness = np.genfromtxt(dir+'/source/Main Results.csv', delimiter = ',',usecols=[4,5], unpack = True)

XSideLength, YSideLength = np.genfromtxt(dir+'/source/Main Results.csv', delimiter = ',',usecols=[6,7], unpack = True)

plt.figure()
plt.plot(XArea, YArea,)
plt.xlabel('Area (mm^2)')
plt.ylabel('Period (s)')
plt.title('Area Vs Period of Oscillation')
plt.savefig(dir+'/results/AreaVsPeriod.png')
plt.close()

plt.figure()
plt.plot(XDensity, YDensity,)
plt.xlabel('Density (g/mm^3)')
plt.ylabel('Period (s)')
plt.title('Density Vs Period of Oscillation')
plt.savefig(dir+'/results/DensityVsPeriod.png')
plt.close()

plt.figure()
plt.plot(XThickness, YThickness,)
plt.xlabel('Thickness (mm)')
plt.ylabel('Period (s)')
plt.title('Thickenss Vs Period of Oscillation')
plt.savefig(dir+'/results/ThicknessVsPeriod.png')
plt.close()

plt.figure()
plt.plot(XSideLength, YSideLength,)
plt.xlabel('Side Length (mm)')
plt.ylabel('Period (s)')
plt.title('Side Length Vs Period of Oscillation')
plt.savefig(dir+'/results/Side_LengthVsPeriod.png')
plt.close()