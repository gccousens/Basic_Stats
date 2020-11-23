# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:00:03 2020

@author: Ginny
"""

def basic_stats(x):
    
    import matplotlib.pyplot as plt
    
    length = 0
    for item in x:
        length = length + 1
    #print(length)
    
    total = 0
    for item in x:
        total = total + item
    #print(total)

    mean = total / length
    print('The mean is: ', mean)

    diffsqrd = []
    for i in x:
        diffsqrd.append((i-mean)**2)
    #print(diffsqrd)

    total2 = 0
    for number in diffsqrd:
        total2 = total2 + number
    #print(total2)

    stdev = (total2 / (length-1)) ** (1/2)
    print('The standard deviation is: ', stdev)
    
    plt.hist(x,)
    plt.xlabel('bins')
    plt.ylabel('Value of number in list')
    plt.show
    return