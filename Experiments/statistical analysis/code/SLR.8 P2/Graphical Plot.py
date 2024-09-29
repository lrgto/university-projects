#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:16:02 2017

@author: lrgtomaszewski
"""

import numpy as np
import matplotlib.pyplot as plt

Displacement_Angle = np.array([5,10,20,30,40,50])
T_Experimental = np.array([1.94, 1.94, 1.98, 2.01, 2.04, 2.08])
T_Theoretical = np.array([2.17,2.64,2.13,2.22,2.56,1.97])

plt.plot(Displacement_Angle,T_Experimental,'x',color='Red',label='Experimental Data of T')
plt.plot(Displacement_Angle,T_Theoretical,'+',color='Blue',label='Theoretical Data of T')
plt.errorbar(Displacement_Angle,T_Experimental,xerr=1,yerr=[0.01, 0.04, 0.11, 0.05, 0.06, 0.07])

plt.xlabel('Displacement Angle (Degrees)')
plt.ylabel('Time (s)')
plt.title('Theoretical & Experimental Data')
plt.legend()
plt.show()