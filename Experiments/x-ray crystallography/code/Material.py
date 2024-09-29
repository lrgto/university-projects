import numpy as np
import matplotlib.pyplot as plt
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

dx1 = np.array([0, 6, 13, 26, 29, 40, 47])
dy1 = np.array([0.000, 2.5941, 34.3015, 204.2926, 332.1887, 210.2156, 305.9509])

plt.figure()
plt.plot(dx1, dy1, 'k')
plt.axis([0, 50, 0, 350])
plt.xlabel('Atomic Number of Materials')
plt.ylabel('Transmittance')
plt.title('Atomic numbers of materials vs transmittance without a Zirconium Filter')
plt.savefig(dir+'/results/Atomic numbers of materials vs transmittance without a Zirconium Filter.png', dpi=300, bbox_inches='tight')

dx2 = np.array([0, 6, 13, 26, 29, 40, 47])
dy2 = np.array([0.000, 2.8470, 52.5747, 192.9249, 372.9804, 175.0904, 347.4163])

plt.figure()
plt.plot(dx2, dy2, 'k')
plt.axis([0, 50, 0, 350])
plt.xlabel('GAtomic Number of Materials')
plt.ylabel('Transmittance')
plt.title('Atomic numbers of materials vs transmittance with a Zirconium Filter')
plt.savefig(dir+'/results/Atomic numbers of materials vs transmittance with a Zirconium Filter.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(dx1, dy1, 'k', label='Without Zirconium Filter')
plt.plot(dx2, dy2, 'r', label='With Zirconium Filter')
plt.axis([0, 50, 0, 350])
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Atomic numbers of materials vs transmittance with and without a Zirconium Filter')
plt.savefig(dir+'/results/Atomic numbers of materials vs transmittance with and without a Zirconium Filter.png', dpi=300, bbox_inches='tight')