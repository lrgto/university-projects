import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x1 = np.array([0.0000, 0.00050, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030])
y1 = np.array([1.0000, 0.4272, 0.2584, 0.1042, 0.0511, 0.0318, 0.0166])

t_s = x1 - x1[0]
log = np.log(y1)
fig,plot = plt.subplots(2,1)

plot[0].axis([0,0.003,0,1])
plot[0].set_ylabel('Transmittance')
plot[0].set_xlabel('Material Thickness')
plot[0].set_title('Linear')

plot[1].axis([0,0.003,-5,1])
plot[1].set_ylabel('Log Transmittance')
plot[1].set_xlabel('Material Thickness')
plot[1].set_title('Natural Log')


def linearFunc(x,m,c):
    y = m * x + c
    return y

fit,cov=curve_fit(linearFunc,t_s,log)

m = fit[0]
c = fit[1]
d_m = np.sqrt(cov[0][0])
d_c = np.sqrt(cov[1][1])
print(m)
print(d_m)
print(c)
print(d_c)

log_fit = m * t_s +c
plot[1].plot(t_s,log_fit)

plt.show()
