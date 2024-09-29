import os, matplotlib.pyplot as plt, pandas as pd

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data = pd.read_csv(f'{dir}/source/Main Results.csv')
x = list(range(1, data.shape[0]+1))        

# Task 1 Individual Bar Plots
for i in list(range(1,data.shape[1]+1)):
    plt.figure()
    plt.bar(x, data[f'Trial {i}'], width=1); plt.xlabel('Bins', labelpad=10); plt.ylabel('Count', labelpad=10); plt.xticks(x)
    plt.title(f'Count of ball bearings falling into {data.shape[0]} bins in trial {i}/{data.shape[1]}', pad=9)
    plt.savefig(f'{dir}/results/T1-Bars-BinsVsCounts(Trial{i}).png', dpi=500, bbox_inches="tight")
    plt.close()
    
# Task 1 Total of all Trials Bar Plot
datasum = data.iloc[:,0:data.shape[1]].sum(axis=1)
plt.figure()
plt.bar(x, datasum, width=1); plt.xlabel('Bins', labelpad=10); plt.ylabel('Count', labelpad=10); plt.xticks(x)
plt.title(f'Count of all {sum(datasum)} ball bearings falling into {data.shape[0]} bins in sum of {data.shape[1]} trials', pad=10, fontsize=10.4)
plt.savefig(f'{dir}/results/T1-Bars-BinsVsCounts(TotalOfTrials).png', dpi=500, bbox_inches="tight")
plt.close()

# Task 1 Total Sum/Trials Bar Plot
plt.figure()
plt.bar(x, (datasum/data.shape[1]), width=1); plt.xlabel('Bins', labelpad=10); plt.ylabel('Count', labelpad=10); plt.xticks(x)
plt.title(f'Count of {sum(datasum)}/{data.shape[1]} ball bearings falling into {data.shape[0]} bins in {data.shape[1]} trials', pad=10, fontsize=11.6)
plt.savefig(f'{dir}/results/T1-Bars-BinsVsCounts(TotalByNoTrials).png', dpi=500, bbox_inches="tight")
plt.close()