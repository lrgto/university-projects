import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

dy1 = np.array([0.91, -0.45, -0.78, 0.99, -0.105,0.153])
dx1 = np.array([3.686, -1.808, -3.180, 4.014, 2.156, 0.777])

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
plt.xlabel('n$\\lambda$')
plt.ylabel('Sin $\\theta$')
plt.title('LiF crystal at 10s showing Sin$\\theta$ vs n$\\lambda$')
plt.plot(dx1,log_fit1)
plt.savefig(dir+'/results/LIF10s', dpi=300, bbox_inches='tight')

dy3 = np.array([0.126, 0.817, 0.365, 0.895, 0.682, -0.187])
dx3 = np.array([0.713, 4.609, 2.059, 5.047, 3.846, -1.059])

def linearFuncd1(x,m,c):
    y = m * x + c
    return y

fit2,cov2=curve_fit(linearFuncd1,dx3,dy3)

m2 = fit2 [0]
c2 = fit2 [1]
d_m2 = np.sqrt(cov2[0])
d_c2 = np.sqrt(cov2[1])
print(m2)
print(d_m2)
print(c2)
print(d_c2)

log_fit2 = m2 * dx3 +c2

plt.figure()
plt.plot(dx3, dy3, 'k')
plt.xlabel('n$\\lambda$')
plt.ylabel('Sin $\\theta$')
plt.title('NaCl crystal at 10s showing Sin$\\theta$ vs n$\\lambda$')
plt.plot(dx3,log_fit2)
plt.savefig(dir+'/results/NACL10s', dpi=300, bbox_inches='tight')