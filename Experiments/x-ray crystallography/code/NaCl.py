import numpy as np
import matplotlib.pyplot as plt
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#------------------------------------------------------------------------------
# NaCl Crystal
#------------------------------------------------------------------------------

NaClx1s, NaCly1s = np.genfromtxt('GraphingDataNaCl.txt',delimiter='',usecols=(0, 1),unpack=True)
NaClx10s, NaCly10s = np.genfromtxt('GraphingDataNaCl.txt',delimiter='',usecols=(2, 3),unpack=True) 

plt.figure()
plt.plot(NaClx1s, NaCly1s, 'k', label='NaCl at 1s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig(dir+'/results/LiF1s.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(NaClx10s, NaCly10s, 'k', label='NaCl at 10s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig(dir+'/results/LiF1s.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(NaClx1s, NaCly1s, 'r', label='NaCl at 1s Interval')
plt.plot(NaClx10s, NaCly10s, 'k', label='NaCl at 10s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig(dir+'/results/LiF1s.png', dpi=300, bbox_inches='tight')