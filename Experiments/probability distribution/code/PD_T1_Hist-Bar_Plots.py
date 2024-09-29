import os, matplotlib.pyplot as plt, pandas as pd

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
datafile = pd.read_csv(dir+'/source/Main Results.csv') 

def plot_hist(data,numbins,xlabel,ylabel,pad,titlefontsize,figtitle,savename):
    plt.figure(); plt.hist(data, bins=numbins); plt.xlabel(xlabel, labelpad=pad); plt.ylabel(ylabel, labelpad=pad); plt.title(figtitle, pad=pad, fontsize=titlefontsize); plt.savefig(dir+'/results/'+savename+'.png', dpi=500, bbox_inches='tight'); plt.close()
    
def plot_bar(x,y,xlabel,ylabel,pad,titlefontsize,figtitle,savename):
    plt.figure(); plt.bar(x,y,width=1); plt.xlabel(xlabel, labelpad=pad); plt.ylabel(ylabel, labelpad=pad); plt.xticks(x); plt.title(figtitle, pad=pad, fontsize=titlefontsize); plt.savefig(dir+'/results/'+savename+'.png', dpi=500,bbox_inches='tight'); plt.close()
    
# Task 1 Histogram Plots (individual, total of all trials, total sum/trials)
for i in list(range(1,datafile.shape[1]+1)):
    plot_hist(datafile[f'Trial {i}'],17,'Counts','Frequency',10,12,f'Frequency of ball bearings falling into {datafile.shape[0]} bins in trial {i}/{datafile.shape[1]}',f'T1-Hist-CountsVsFrequency(Trial{i})')

plot_hist((datafile.iloc[:,0:datafile.shape[1]].sum(axis=1)),17,'Counts','Frequency',10,9.8,f'Frequency of all {sum(datafile.iloc[:,0:datafile.shape[1]].sum(axis=1))} ball bearings falling into {datafile.shape[0]} bins in sum of {datafile.shape[1]} trials','T1-Hist-CountsVsFrequency(TotalOfTrials)')
plot_hist(((datafile.iloc[:,0:datafile.shape[1]].sum(axis=1))/datafile.shape[1]),17,'Counts','Frequency',10,10.7,f'Frequency of {sum(datafile.iloc[:,0:datafile.shape[1]].sum(axis=1))}/{datafile.shape[1]} ball bearings falling into {datafile.shape[0]} bins in {datafile.shape[1]} trials','T1-Hist-CountsVsFrequency(TotalByNoTrials)')

# Task 1 Bar Plots (individual, total of all trials, total sum/trials)
for i in list(range(1,datafile.shape[1]+1)):
    plot_bar((list(range(1, datafile.shape[0]+1))),datafile[f'Trial {i}'],'Bins','Count',10,12, f'Count of ball bearings falling into {datafile.shape[0]} bins in trial {i}/{datafile.shape[1]}',f'T1-Bars-BinsVsCount(Trial{i})')
    #plt.bar((list(range(1, datafile.shape[0]+1))),datafile[f'Trial {i}'],1,color=None); plt.xlabel('Bins', labelpad=10); plt.ylabel('Count', labelpad=10); plt.xticks((list(range(1, datafile.shape[0]+1)))); plt.title(f'Count of ball bearings falling into {datafile.shape[0]} bins in {datafile.shape[1]} trials comparison', pad=10, fontsize=11); plt.savefig(dir+'/results/T1-Bars-BinsVsCountAllTrialsComparison.png', dpi=500, bbox_inches='tight')

plot_bar((list(range(1, datafile.shape[0]+1))),(datafile.iloc[:,0:datafile.shape[1]].sum(axis=1)),'Bins','Count',10,10.4,f'Count of all {sum(list(range(1, datafile.shape[0]+1)))} ball bearings falling into {datafile.shape[0]} bins in sum of {datafile.shape[1]} trials','T1-Bars-BinsVsCount(TotalOfTrials)')
plot_bar((list(range(1, datafile.shape[0]+1))), ((datafile.iloc[:,0:datafile.shape[1]].sum(axis=1))/datafile.shape[1]),'Bins','Count',10,11.6,f'Count of {sum(list(range(1, datafile.shape[0]+1)))}/{datafile.shape[1]} ball bearings falling into {datafile.shape[0]} bins in {datafile.shape[1]} trials','T1-Bars-BinsVsCount(TotalByNoTrials)')