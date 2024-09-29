#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:07:09 2017

@author: lrgtomaszewski
"""
import numpy as np

tally_stick = 0
tally_switch = 0

for x in range(10000):
    stay = np.random.randint(1,4)
    swap = np.random.randint(1,4)
    
    if stay == swap:
        tally_stick += 1
    else:
        tally_switch += 1

print('Tally Stick:')
print(tally_stick)
print('Tally Switch:')
print(tally_switch)

probability_win_if_stay = (tally_stick/x)
print('Prob of Stay:')
print(probability_win_if_stay)

probability_win_if_swap = (tally_switch/x)
print('Prob of Swap:')
print(probability_win_if_swap)