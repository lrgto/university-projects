import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

dx1 = np.array([0.0000, 0.00050, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030])
dy1 = np.array([1.0000, 0.4272, 0.2584, 0.1042, 0.0511, 0.0318, 0.0166])

def linearFuncd(x,m,c):
    y = m * x + c
    return y

fit1,cov1=curve_fit(linearFuncd,dx1,dy1)

m1 = fit1 [0]
c1 = fit1 [1]
d_m1 = np.sqrt(cov1[0])
d_c1 = np.sqrt(cov1[1])
print(m1)
print(d_m1)
print(c1)
print(d_c1)

log_fit1 = m1 * dx1 +c1

plt.figure()
plt.plot(dx1, dy1, 'k')
plt.xlabel('Thickness (m)')
plt.ylabel('Transmittance')
plt.title('Linear transmittance vs thickness without a Zirconium filter')
plt.plot(dx1,log_fit1)
plt.savefig(dir+'/results/Linear transmittance vs thickness without a Zirconium filter.png', dpi=300, bbox_inches='tight')

a1 = np.polyfit(dx1.flatten(), dy1.flatten(), 1)
b1 = np.poly1d(a1)

print("y=%.6fx+%.6f"%(a1[0], a1[1]))

plt.figure()
plt.loglog(dx1, dy1, 'k')
plt.xlabel('Thickness (m)')
plt.ylabel('Transmittance')
plt.title('Log transmittance vs thickness without a Zirconium filter')
plt.loglog(dx1,b1(dx1))
plt.savefig(dir+'/results/Log transmittance vs thickness without a Zirconium filter.png', dpi=300, bbox_inches='tight')



dy3 = np.array([1.0000, 0.4026, 0.1889, 0.0842, 0.0245, 0.0189, 0.0093])

def linearFuncd1(x,m,c):
    y = m * x + c
    return y

fit2,cov2=curve_fit(linearFuncd1,dx1,dy3)

m2 = fit2 [0]
c2 = fit2 [1]
d_m2 = np.sqrt(cov2[0])
d_c2 = np.sqrt(cov2[1])
print(m2)
print(d_m2)
print(c2)
print(d_c2)

log_fit2 = m2 * dx1 +c2

plt.figure()
plt.plot(dx1, dy3, 'k')
plt.xlabel('Thickness (m)')
plt.ylabel('Transmittance')
plt.title('Linear transmittance vs thickness with a Zirconium filter')
plt.plot(dx1,log_fit2)
plt.savefig(dir+'/results/Linear transmittance vs thickness with a Zirconium filter.png', dpi=300, bbox_inches='tight')

a2 = np.polyfit(dx1.flatten(), dy3.flatten(), 1)
b2 = np.poly1d(a2)

print("y=%.6fx+%.6f"%(a2[0], a2[1]))

plt.figure()
plt.loglog(dx1, dy3, 'k')
plt.xlabel('Thickness (m)')
plt.ylabel('Transmittance')
plt.title('Log transmittance vs thickness with a Zirconium filter')
plt.loglog(dx1,b2(dx1))
plt.savefig(dir+'/results/Log transmittance vs thickness with a Zirconium filter.png', dpi=300, bbox_inches='tight')




plt.figure()
plt.plot(dx1, dy1, 'k', label='Without Zirconium Filter')
plt.plot(dx1, dy3, 'r', label='With Zirconium Filter')
plt.xlabel('Thickness (m)')
plt.ylabel('Transmittance')
plt.title('Linear transmittance vs thickness with/out a Zirconium filter comparison')
plt.legend(loc='best')
plt.savefig(dir+'/results/Linear transmittance vs thickness with and without a Zirconium filter comparison.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.loglog(dx1, dy1, 'k', label='Without Zirconium Filter')
plt.loglog(dx1, dy3, 'r', label='With Zirconium Filter')
plt.xlabel('Thickness (m)')
plt.ylabel('Transmittance')
plt.title('Log transmittance vs thickness with/out a Zirconium filter comparison')
plt.legend(loc='best')
plt.savefig(dir+'/results/Log transmittance vs thickness with and without a Zirconium filter comparison.png', dpi=300, bbox_inches='tight')