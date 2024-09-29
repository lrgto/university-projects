#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:23:23 2017

@author: lrgtomaszewski
"""

import random

DOORS = (1,2,3)

def hallpicker(strategy):
    prize = random.choice(DOORS)
    firstchoice = random.choice(DOORS)
    if strategy == 'stay':
        return firstchoice == prize
    elif strategy == 'switch':
        hostchoice = random.choice([x for x in DOORS if x != firstchoice and x != prize])
        secondchoice = [x for x in DOORS if x != firstchoice and x != hostchoice]
        assert len(secondchoice) == 1
        return secondchoice[0] == prize
    else:
        raise ValueError

def counter(strategy, n=10000):
    return sum(hallpicker(strategy) for i in xrange(n))/float(n)

if __name__ == "__main__":
    print "stay:", counter('stay')
    print "switch:", counter('switch')
    