#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:16:02 2017

@author: lrgtomaszewski
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('Data Set 1.csv')

mybins = np.arange(2.13,1.18,0.05)
#Range =           Max, Min, Bin

plt.hist(data,bins=mybins)
plt.xlabel('Time Taken')
plt.ylabel('Frequency')
plt.savefig('Histogram of Data 1.png')

plt.clf()

data = np.genfromtxt('Data Set 2.csv')

mybins = np.arange(2.15,1.68,0.05)
#Range =           Max, Min, Bin

plt.hist(data,bins=mybins)
plt.xlabel('Time Taken')
plt.ylabel('Frequency')
plt.savefig('Histogram of Data 2.png')
