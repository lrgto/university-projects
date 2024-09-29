import os, matplotlib.pyplot as plt, numpy as np

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def plt_fig(pltdata, xlabel='',ylabel='',plttitle='', pltlegend='', pltsave=''):
        plt.xlabel(xlabel); plt.ylabel(ylabel); plt.title(plttitle); plt.legend(loc=pltlegend); plt.savefig(pltsave, dpi=500, format='png')
        
# Q2.1.1 Theory Results
x = (-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30)
yt = []
for i in x:
        ya = 1/(np.sin(i/2))**4; yt.append(ya)
yt[6] = 0

# Q2.1.1 Actual Results
y = (0.117,0.200,0.550,4.767,24.117,44.617,50.067,44.700,25.767,5.700,1.150,0.300,0.083)
xerror, yerror = 1.5, 0.100

# Q2.1.1 Plot
plt.figure()
plt.loglog(x,yt,'-b',label='Theoretical Results')
plt.loglog(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.title('Angle of Deflection vs No. of Particles (Gate Time = 10s)')
plt.xlabel('Angle of Deflection ($\Theta$)')
plt.ylabel('No. of Particles ($NA_1$)')
plt.legend(loc='best')
plt.savefig(f'{dir}/results/211Angle_v_particles_at_10s.png')
plt.close()

# Q2.2.2 Actual Results
y = (0.092,0.231,1.085,4.060,22.590,43.515,62.500,43.810,27.010,8.240,1.145,0.371,0.141)
xerror, yerror= 1.5, 0.001

# Q2.2.2 Plot
plt.figure()
plt.plot(x,y,'-r',label='Actual Results')
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='-r', ecolor='red', capsize=1)
plt.xlabel('Angle of Deflection ($\Theta$)')
plt.ylabel('Rate of Particles ($NA_1/s$)')
plt.title('Angle of Deflection vs Rate of Particles (Gate Time = 40s)')
plt.savefig(f'{dir}/results/212Angle_v_particles_rate_at_40s.png')
plt.close()