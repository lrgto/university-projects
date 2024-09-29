# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

y7 = [0,0,0,0,0,0,0,0,0.3930,0]
y6 = [0,0,0,0.0033,0,0.1357,0,0,0.9024,0]
y4 = [0,0,0.9280,0.9478,0,0.9588,0.9280,0,0.9742,0.9280]
y1 = [0.9842,0.9842,0.9925,0.9929,0.9788,0.9932,0.9925,0.9842,0.9938,0.9925]
y8 = [0,0,0,0,0,0,0,0,0.0009,0]
x0 = [0,1,2,3,4,5,6,7,8,9]

plt.figure()
plt.plot(x0,y7, color="black", label='$g_{bar-L}$ = 7')
plt.plot(x0,y6, color="red", label='$g_{bar-L}$ = 6')
plt.plot(x0,y4, color="blue", label='$g_{bar-L}$ = 4')
plt.plot(x0,y1, color="green", label='$g_{bar-L}$ = 1')
plt.plot(x0,y8, color="orange", label='$g_{bar-L}$ = 8')
plt.xlabel('Digits')
plt.ylabel('Recieving Value')
plt.legend(loc='best')
plt.title('Recieving values of digits 0-9 dependent on $g_{bar-l}$ value')
plt.savefig('Q2.9B.png', dpi=500, bbox_inches='tight')