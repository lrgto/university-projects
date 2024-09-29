#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:31:44 2017

@author: lrgtomaszewski
"""

n = int(input("Enter the number of iterations: "))

winswap = 0.0
winnoswap = 0.0
simcount = 0.0

for i in range(n):
    simcount = simcount + 1
    picked_door = random.randint(1,3)
    car = random.randint(1,3)
    g = random.randint(1,3)

    completed = False 
    while not completed:
        if g != car and g != picked_door:
            completed = True
        else:
            g = random.randint(1,3)      

    swap = random.randint(1,2)


    if swap == 2:
        if g != 1 and picked_door != 1:
            picked_door = 1
        elif g != 2 and picked_door != 2:
            picked_door = 2
        else:
            picked_door = 3 



    if picked_door == car and swap == 1:
        winnoswap = winnoswap + 1
    if picked_door == car and swap == 2:
        winswap = winswap + 1

print ("The amount of no swap wins is", winnoswap)
print ("The amount of swap wins is", winswap)

total_wins = winnoswap + winswap

percentswap = (winswap/total_wins)*100
percentnoswap = (winnoswap/total_wins)*100

print ("Percentage wins of swapping is", percentswap,"%")
print ("Percentage wins of not swapping is", percentnoswap,"%")