#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:17:49 2018

@author: lrgtomaszewski
"""

import matplotlib.pyplot as plt
import csv

with open('4.1 Graph Figures.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')


plt.plot(x,y, marker='o')

plt.title('Data from the CSV File: People and Expenses')

plt.xlabel('Number of People')
plt.ylabel('Expenses')

plt.show()
