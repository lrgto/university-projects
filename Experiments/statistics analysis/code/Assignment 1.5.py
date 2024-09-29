#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:21:00 2017

@author: lrgtomaszewski
"""

import numpy as np

p_A = 0.95 
p_B = 0.95
p_C = 0.90  
p_D = 0.90  
p_E = 0.80  

np.random.rand()

failed_cases=0

n=1000000

for i in range(n):
    r_A = np.random.rand() < p_A
    r_B = np.random.rand() < p_B
    r_C = np.random.rand() < p_C
    r_D = np.random.rand() < p_D
    r_E = np.random.rand() < p_E
        
    if (r_A + r_B + r_C + r_D + r_E<3):
        failed_cases+=1

print(failed_cases)

print("Probability of Wrong Verdict")
print(failed_cases/n)

        