import os,  numpy as np, matplotlib.pyplot as plt

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

xs, ys = np.genfromtxt(dir+'/source/AST_Data.txt',delimiter='',unpack=True) 
plt.figure()
plt.plot(xs,ys) 
plt.xlabel('Pixel Value')
plt.ylabel('Pixel ADUs')
plt.title('AST Spectrum Data Graph \n (AIP4WIN AST_rot_tr.fits Spectroscopy Data)')
plt.savefig(dir+'/results/AST_Data_Graph.png', dpi=300, bbox_inches='tight')

xz, yz = np.genfromtxt(dir+'/source/HeAr_Data.txt',delimiter='',unpack=True) 
plt.figure()
plt.plot(xz,yz) 
plt.xlabel('Pixel Value')
plt.ylabel('Pixel ADUs')
plt.title('HeAr Spectrum Data Graph \n (AIP4WIN HeAr_rot_tr.fits Spectroscopy Data)')
plt.savefig(dir+'/results/HeAr_Data_Graph.png', dpi=300, bbox_inches='tight')

xr, yr = np.genfromtxt(dir+'/source/SA_Data.txt',delimiter='',unpack=True) 
plt.figure()
plt.plot(xr,yr) 
plt.xlabel('Pixel Value')
plt.ylabel('Pixel ADUs')
plt.title('SA Spectrum Data Graph \n (AIP4WIN SA_rot_tr.fits Spectroscopy Data)')
plt.savefig(dir+'/results/SA_Data_Graph.png', dpi=300, bbox_inches='tight')