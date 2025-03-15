# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:27:59 2024

@author: Vamsi
"""
import math
def findMaximumQuality( packets, channels ):
    packets.sort(reverse = True)
    res = 0
    for i in range(channels-1):
        res += packets[i]
    start, end = channels-1, len(packets)-1
    count = end-start+1
    if count%2 == 0:
        first = start + (end-start)//2
        second = first + 1
        res += math.ceil((packets[first]+packets[second])/2)
    else:
        index = start + (end-start)//2
        res += packets[index]
    
    return res

packets = [ 5, 2, 2, 1, 5, 3 ] # [1, 2, 3, 4, 5]
channels = 2

res = findMaximumQuality(packets, channels)

print( res )