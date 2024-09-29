import numpy as np
import matplotlib.pyplot as plt
import os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#------------------------------------------------------------------------------

xc1, yc1 = np.genfromtxt(dir+'/source/ThickData.txt',delimiter='',usecols=(0, 1),unpack=True)
xc1, yc2 = np.genfromtxt(dir+'/source/ThickData.txt',delimiter='',usecols=(0, 2),unpack=True) 
xc1, yc3 = np.genfromtxt(dir+'/source/ThickData.txt',delimiter='',usecols=(0, 3),unpack=True) 
xc1, yc4 = np.genfromtxt(dir+'/source/ThickData.txt',delimiter='',usecols=(0, 4),unpack=True) 
xerror = 0.0
yerror1 = np.sqrt(yc1)
yerror2 = np.sqrt(yc2)
yerror3 = np.sqrt(yc3)
yerror4 = np.sqrt(yc4) 
plt.figure()
plt.plot(xc1,yc1, 'k', label='0.9mm Lead')
plt.errorbar(xc1, yc1, xerr=xerror, yerr=yerror1, fmt='-k', ecolor='black', capsize=1) 
plt.plot(xc1,yc2, 'r', label='2.2mm Lead')
plt.errorbar(xc1, yc2, xerr=xerror, yerr=yerror2, fmt='-r', ecolor='red', capsize=1)
plt.plot(xc1,yc3, 'g', label='5.5mm Lead')  
plt.errorbar(xc1, yc3, xerr=xerror, yerr=yerror3, fmt='-g', ecolor='green', capsize=1)
plt.plot(xc1,yc4, 'b', label='10mm Lead') 
plt.errorbar(xc1, yc4, xerr=xerror, yerr=yerror4, fmt='-b', ecolor='blue', capsize=1)
plt.xlabel('Channels')
plt.ylabel('Counts')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
plt.savefig(dir+'/results/CobaltLeadCounts.png', dpi=300, bbox_inches='tight')

#------------------------------------------------------------------------------
# FINAL GRAPHS
#------------------------------------------------------------------------------

x = 0.0009, 0.0022, 0.0055, 0.0170
yl117 = 3.07, 3.09, 3.25, 3.81
yl133 = 3.00, 3.01, 3.07, 3.32
ya117 = 3.19, 3.22, 3.32, 3.70
ya133 = 3.04, 3.08, 3.18, 3.52
yl066 = 22.45, 47.61, 111.51, 334.37
ya066 = 8.92, 14.56, 28.88, 78.77

xerror = 0.00002
yerrorl117 = 1.51, 1.49, 1.49, 1.49
yerrorl133 = 1.49, 1.48, 1.48, 1.48
yerrora117 = 1.58, 1.57, 1.57, 1.57
yerrora133 = 1.51, 1.51, 1.51, 1.49
yerrorl066 = 2.53, 2.55, 2.62, 2.94
yerrora066 = 2.51, 2.52, 2.54, 2.60

plt.figure()
plt.plot(x,yl117, 'k') 
plt.errorbar(x, yl117, xerr=xerror, yerr=yerrorl117, fmt='-k', ecolor='black', capsize=1) 
plt.xlabel('Thickness (Metres)')
plt.ylabel('Counts')
plt.title('Cobalt (¢1.17MeV¢) Lead thickness vs Counts comparison')
plt.savefig(dir+'/results/CobaltLead117Final.png', dpi=300, bbox_inches='tight')