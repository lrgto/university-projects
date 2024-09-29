import csv
import matplotlib.pylab as plt
import os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def getColumn(filename, column):
    results = csv.reader(open(filename), dialect='excel')
    return [result[column] for result in results]
# This allows the script to identify nad isolate columns in data
# files, as specified data file have 3 columns and this only 
# having need of 2 of them.

BI_Its = getColumn(dir+"/source/Bi-Section.csv",0) 
BI_Per = getColumn(dir+"/source/Bi-Section.csv",2)
# This section allows the script to input data from an external 
# source, the 0 and 2 are to isolate the data from 2 specific
# columns i.e. number of iteration and percentage difference.


NR_Its = getColumn(dir+"/source/Newton Raphson.csv",0)
NR_Per = getColumn(dir+"/source/Newton Raphson.csv",2)
# This section allows the script to input data from an external 
# source, the 0 and 2 are to isolate the data from 2 specific 
# columns i.e. number of iteration and percentage difference.

plt.semilogy(BI_Its,BI_Per, 'k', label='Bi-Section')
plt.plot(NR_Its, NR_Per, label='Newton Raphson')
# Plots both sets of data together on the same graph.

plt.xlabel('Number of Iterations')
plt.ylabel('Percentage Difference')
plt.title('Numerical Methods Graph')
# Labels to identify both axes.

plt.legend()
# To identify which sets of data belong to which script.

plt.savefig(dir+'/results/Numerical Methods Graph.png')
# Externally saving the png image on its own for further 
# analysis.

plt.show()
