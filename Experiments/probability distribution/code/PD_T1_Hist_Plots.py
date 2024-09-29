import os, matplotlib.pyplot as plt, pandas as pd

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data = pd.read_csv(f'{dir}/source/Main Results.csv')

# Task 1 Individual Histogram Plots
for i in list(range(1,data.shape[1]+1)):
    plt.figure()
    plt.hist(data[f'Trial {i}'],17); plt.xlabel('Counts', labelpad=10); plt.ylabel('Frequency', labelpad=10)
    plt.title(f'Frequency of ball bearings falling into {data.shape[0]} bins in trial {i}/{data.shape[1]}', pad=9)
    plt.savefig(f'{dir}/results/T1-Hist-CountsVsFrequency(Trial{i}).png', dpi=500, bbox_inches="tight")
    plt.close()

# Task 1 Total of all Trials Histogram Plot
datasum = data.iloc[:,0:data.shape[1]].sum(axis=1)
plt.figure()
plt.hist(datasum,17); plt.xlabel('Counts', labelpad=10); plt.ylabel('Frequency', labelpad=10)
plt.title(f'Frequency of all {sum(datasum)} ball bearings falling into {data.shape[0]} bins in sum of {data.shape[1]} trials', pad=10, fontsize=9.8)
plt.savefig(f'{dir}/results/T1-Hist-CountsVsFrequency(TotalOfTrials).png', dpi=500, bbox_inches="tight")
plt.close()

# Task 1 Total Sum/Trials Histogram Plot
plt.figure()
plt.hist((datasum/data.shape[1]),17); plt.xlabel('Counts', labelpad=10); plt.ylabel('Frequency', labelpad=10)
plt.title(f'Frequency of {sum(datasum)}/{data.shape[1]} ball bearings falling into {data.shape[0]} bins in {data.shape[1]} trials', pad=10, fontsize=10.7)
plt.savefig(f'{dir}/results/T1-Hist-CountsVsFrequency(TotalByNoTrials).png', dpi=500, bbox_inches="tight")
plt.close()