import os,  numpy as np, matplotlib.pyplot as plt

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

xs, ys = np.genfromtxt(dir+'/source/Vega_Data.txt',delimiter='',unpack=True) 
plt.figure()
plt.plot(xs,ys) 
plt.xlabel('Pixel Value')
plt.ylabel('Pixel Count')
plt.title('Vega Spectrum (Pixel Count Vs Pixel Value)')
plt.savefig(dir+'/results/Vega_Spectrum(Count_Vs_Value).png', dpi=500, bbox_inches='tight')