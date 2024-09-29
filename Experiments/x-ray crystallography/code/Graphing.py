import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#------------------------------------------------------------------------------
# Data 1
#------------------------------------------------------------------------------

dx1 = np.array([0.0000, 0.00050, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030])
dy1 = np.array([1.0000, 0.4272, 0.2584, 0.1042, 0.0511, 0.0318, 0.0166])
log1 = np.log(dy1)

def linearFuncd1(x,m,c):
    y = m * x + c
    return y

fit1,cov1=curve_fit(linearFuncd1,dx1,dy1)

def linearFuncd1log(x,m,c):
    y = m * x + c
    return y

fit1log,cov1log=curve_fit(linearFuncd1log,dx1,dy1)

m = fit1, fit1log
c = fit1, fit1log
d_m = np.sqrt(cov1, cov1log)
d_c = np.sqrt(cov)
print(m)
print(d_m)
print(c)
print(d_c)

log_fit = m * dx1 +c

plt.figure()
plt.axis([0,0.003,0,1])
plt.plot(dx1, dy1, 'k', label='LiF at 1s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
plt.plot(dx1,log_fit)
plt.savefig(dir+'/results/LiF1s.png', dpi=300, bbox_inches='tight')

dx2 = np.array([0.0000, 0.00050, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030])
dy2 = np.array([1.0000, 0.4272, 0.2584, 0.1042, 0.0511, 0.0318, 0.0166])

def linearFuncd1(x,m,c):
    y = m * x + c
    return y

fit2,cov2=curve_fit(linearFuncd1,dx1,dy1)

m = fit[0]
c = fit[1]
d_m = np.sqrt(cov[0][0])
d_c = np.sqrt(cov[1][1])
print(m)
print(d_m)
print(c)
print(d_c)

log_fit1 = m * dx1 +c

plt.figure()
plt.axis([0,0.003,0,1])
plt.plot(dx1, dy1, 'k', label='LiF at 1s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
plt.plot(dx2,log_fit1)
plt.savefig(dir+'/results/LiF1s.png', dpi=300, bbox_inches='tight')
































#------------------------------------------------------------------------------
# LiF Crystal
#------------------------------------------------------------------------------

LiFx1s, LiFy1s = np.genfromtxt('GraphingData.txt',delimiter='',usecols=(0, 1),unpack=True)
LiFx10s, LiFy10s = np.genfromtxt('GraphingData.txt',delimiter='',usecols=(2, 3),unpack=True) 

plt.figure()
plt.plot(LiFx1s, LiFy1s, 'k', label='LiF at 1s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig('LiF1s.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(LiFx10s, LiFy10s, 'k', label='LiF at 10s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig('LiF10s.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(LiFx1s, LiFy1s, 'r', label='LiF at 1s Interval')
plt.plot(LiFx10s, LiFy10s, 'k', label='LiF at 10s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig('LifComparision.png', dpi=300, bbox_inches='tight')

#------------------------------------------------------------------------------
# Corrected LiF Crystal
#------------------------------------------------------------------------------

NaClx1s, NaCly1s = np.genfromtxt('GraphingData.txt',delimiter='',usecols=(4, 5),unpack=True)
NaClx10s, NaCly10s = np.genfromtxt('GraphingData.txt',delimiter='',usecols=(6, 7),unpack=True) 

plt.figure()
plt.plot(NaClx1s, NaCly1s, 'k', label='NaCl at 1s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig('LiF1s.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(NaClx10s, NaCly10s, 'k', label='NaCl at 10s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig('LiF1s.png', dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(NaClx1s, NaCly1s, 'r', label='NaCl at 1s Interval')
plt.plot(NaClx10s, NaCly10s, 'k', label='NaCl at 10s Interval')
plt.xlabel('Glancing Angle ($\Theta$)')
plt.ylabel('Counts ($R_0/1s$)')
plt.legend(loc='best')
plt.title('Cobalt Lead thickness counts vs channels comparison')
#plt.savefig('LiF1s.png', dpi=300, bbox_inches='tight')

#------------------------------------------------------------------------------
# FINAL GRAPHS
#------------------------------------------------------------------------------

#plt.figure()
#plt.plot(x,yl117, 'k') 
#plt.errorbar(x, yl117, xerr=xerror, yerr=yerrorl117, fmt='-k', ecolor='black', capsize=1) 
#plt.xlabel('Thickness (Metres)')
#plt.ylabel('Counts')
#plt.title('Cobalt (¢1.17MeV¢) Lead thickness vs Counts comparison')
#plt.savefig('CobaltLead117Final.png', dpi=300, bbox_inches='tight')

#xl, yl = np.genfromtxt('AST.txt',delimiter='',unpack=True) 
#xf, yf = np.genfromtxt('A4 AST.txt',delimiter='',unpack=True) 
#plt.figure()
#plt.plot(xl, yl, label='AST Data')
#plt.plot(xf, yf, label='AST Normalised Data')
#plt.xlabel('Pixel Value')
#plt.ylabel('Pixel ADUs')
#plt.legend(loc='best')
#plt.title('AST Vs AST  Normalised Spectrum Data Graph')
#plt.savefig('ASTVsASTCorPythonGraph.png', dpi=300, bbox_inches='tight')
