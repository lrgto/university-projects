import os, numpy as np, matplotlib.pyplot as plt, pandas as pd, scipy.special

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
datafile= pd.read_csv(dir+'/source/Main Results.csv') 

# Estimated Data
trials_num, bins_num, balls_num = 10, 17, 500; balls_total = trials_num * balls_num
locations_trial, locations_total = np.zeros(balls_num), np.zeros(balls_total)
x = np.arange(1,1+bins_num,1,dtype=int)

for i in range(bins_num):
	shift = np.random.randint(0, 2, size = balls_total); locations_total += shift

plt.figure()
plt.hist(locations_total,bins=np.arange(-0.5,1+bins_num,1),histtype='step')
plt.xticks(x)
plt.xlabel('Bins', labelpad=10)
plt.ylabel('Count', labelpad=10)
plt.title(f'Title', pad=10, fontsize=11.6)
plt.savefig(f'{dir}/results/T2-Hist-Estimated.png', dpi=500, bbox_inches="tight")
plt.close()

# Theorectical Data
theory_values = np.zeros(bins_num+1)

for k in range(0,bins_num+1):
	theory_values[k] = balls_total * scipy.special.binom(bins_num, k) * 0.5**k * 0.5**(bins_num - k)

plt.figure()
plt.bar(range(0,bins_num+1),theory_values,1)
plt.xticks(x)
plt.xlabel('Bins', labelpad=10)
plt.ylabel('Count', labelpad=10)
plt.title(f'Title', pad=10, fontsize=11.6)
plt.savefig(f'{dir}/results/T2-Bars-Theoretical.png', dpi=500, bbox_inches="tight")
plt.close()

# Actual Data
data = datafile.iloc[:,0:datafile.shape[1]].sum(axis=1)
plt.figure()
plt.bar(x, data, width=1)
plt.xlabel('Bins', labelpad=10)
plt.ylabel('Count', labelpad=10)
plt.xticks(x)
plt.title(f'', pad=10, fontsize=10.4)
plt.savefig(f'{dir}/results/T2-Bars-Actual.png', dpi=500, bbox_inches="tight")
plt.close()

# Estimated & Theorectical Data
plt.figure()
plt.hist(locations_total,bins=np.arange(-0.5,1+bins_num,1),histtype='step',label='Estimated')
plt.bar(range(0,bins_num+1),theory_values,1,color='white',fill=False,edgecolor='red',label='Theoretical')
plt.xticks(x)
plt.xlabel('Bins', labelpad=10)
plt.ylabel('Count', labelpad=10)
plt.legend(loc='best')
plt.title(f'Title', pad=10, fontsize=11.6)
plt.savefig(f'{dir}/results/T2-Hist-Bars-Estimated-Theoretical.png', dpi=500, bbox_inches="tight")
plt.close()

# Estimated & Actual Data
plt.figure()
plt.hist(locations_total,bins=np.arange(-0.5,1+bins_num,1), edgecolor='red', histtype='step',label='Estimated')
plt.bar(x, data, width=1, color='white',fill=False, edgecolor='C0', label='Actual')
plt.xticks(x)
plt.xlabel('Bins', labelpad=10)
plt.ylabel('Count', labelpad=10)
plt.legend(loc='best')
plt.title(f'Title', pad=10, fontsize=11.6)
plt.savefig(f'{dir}/results/T2-Hist-Bars-Estimated-Actual.png', dpi=500, bbox_inches="tight")
plt.close()

# Theorectical & Actual Data
plt.figure()
plt.bar(range(0,bins_num+1),theory_values,1,color='white',fill=False,edgecolor='red',label='Theoretical')
plt.bar(x, data, width=1, color='white',fill=False, edgecolor='C0',label='Actual')
plt.xticks(x)
plt.xlabel('Bins', labelpad=10)
plt.ylabel('Count', labelpad=10)
plt.legend(loc='best')
plt.title(f'Title', pad=10, fontsize=11.6)
plt.savefig(f'{dir}/results/T2-Bars-Theoretical-Actual.png', dpi=500, bbox_inches="tight")
plt.close()