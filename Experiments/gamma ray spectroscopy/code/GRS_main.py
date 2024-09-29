import os, numpy as np, matplotlib.pyplot as plt

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Count Graphs

labels = ['Cobalt-Lead-Thickness', 'Cesium-Lead-Thickness', 'Colbalt-Aluminium-Thickness', 'Cesium-Aluminium-Thickness']
labellistplus = ['Lead', 'Lead', 'Aluminium', 'Aluminium', ' ']
labellist = ['0.9mm', '2.2mm', '5.5mm', '10mm']
a, b, c, d, e= 0, 1, 2, 3, 4
labellistend = labellistplus[0]
count = 0

for i in labels:
    x, y1, y2, y3, y4 = np.genfromtxt(dir+'/source/ThickData.txt', delimiter='', usecols=(a, b, c, d, e), unpack=True)
    xerr, yerr1, yerr2, yerr3, yerr4 = 0.0, np.sqrt(y1), np.sqrt(y2), np.sqrt(y3), np.sqrt(y4)

    plt.figure(figsize=(20,15))
    plt.plot(x,y1, 'k', label=f'{labellist[0]} {labellistend}'); plt.errorbar(x, y1, xerr=xerr, yerr=yerr1, fmt='-k', ecolor='black', capsize=1) 
    plt.plot(x,y2, 'r', label=f'{labellist[1]} {labellistend}'); plt.errorbar(x, y2, xerr=xerr, yerr=yerr2, fmt='-r', ecolor='red', capsize=1)
    plt.plot(x,y3, 'g', label=f'{labellist[2]} {labellistend}'); plt.errorbar(x, y3, xerr=xerr, yerr=yerr3, fmt='-g', ecolor='green', capsize=1)
    plt.plot(x,y4, 'b', label=f'{labellist[3]} {labellistend}'); plt.errorbar(x, y4, xerr=xerr, yerr=yerr4, fmt='-b', ecolor='blue', capsize=1)
    plt.xlabel('Channels'); plt.ylabel('Counts'); plt.legend(loc='best')
    plt.title(f'{i} Counts vs Channels Comparison')
    plt.savefig(dir+'/results/{i}.png', dpi=1000, bbox_inches='tight')
    plt.close()
    
    a, b, c, d, e = a+5, b+5, c+5, d+5, e+5
    count = count+1
    labellistend = labellistplus[count]
    
        


# Energy Graphs
'''
labels = ['Cobalt-Lead-Thickness', 'Cesium-Lead-Thickness', 'Colbalt-Aluminium-Thickness', 'Cesium-Aluminium-Thickness','Cobalt-Lead-Energy', 'Cesium-Lead-Energy', 'Colbalt-Aluminium-Energy', 'Cesium-Aluminium-Energy']
datasetlist = ['ThickData','ThickData','ThickData','ThickData','EnergyData','EnergyData','EnergyData1','EnergyData1']
labellistplus = ['Lead', 'Lead', 'Aluminium', 'Aluminium', 'Lead', 'Lead', 'Aluminium', 'Aluminium']
labellist = ['0.9mm', '2.2mm', '5.5mm', '10mm']
a, b, c, d, e= 0, 1, 2, 3, 4
labellistend = labellistplus[0]
dataset = datasetlist[0]

for i in labels:
    x, y1, y2, y3, y4 = np.genfromtxt(dir+'/source/{dataset}.txt', delimiter='', usecols=(a, b, c, d, e), unpack=True)
    xerr, yerr1, yerr2, yerr3, yerr4 = 0.0, np.sqrt(y1), np.sqrt(y2), np.sqrt(y3), np.sqrt(y4)

    plt.figure()
    plt.plot(x,y1, 'k', label=f'{labellist[0]} {labellistend}'); plt.errorbar(x, y1, xerr=xerr, yerr=yerr1, fmt='-k', ecolor='black', capsize=1) 
    plt.plot(x,y2, 'r', label=f'{labellist[1]} {labellistend}'); plt.errorbar(x, y2, xerr=xerr, yerr=yerr2, fmt='-r', ecolor='red', capsize=1)
    plt.plot(x,y3, 'g', label=f'{labellist[2]} {labellistend}'); plt.errorbar(x, y3, xerr=xerr, yerr=yerr3, fmt='-g', ecolor='green', capsize=1)
    plt.plot(x,y4, 'b', label=f'{labellist[3]} {labellistend}'); plt.errorbar(x, y4, xerr=xerr, yerr=yerr4, fmt='-b', ecolor='blue', capsize=1)
    plt.xlabel('Channels'); plt.ylabel('Counts'); plt.legend(loc='best')
    plt.title(f'{i} Counts vs Channels Comparison')
    plt.savefig(dir+'/results/{i}.png', dpi=500, bbox_inches='tight')
    plt.close()
    
    
    a, b, c, d, e = a+5, b+5, c+5, d+5, e+5
    labellistend = labellistplus[0+1]
    dataset = datasetlist[0+1]
'''