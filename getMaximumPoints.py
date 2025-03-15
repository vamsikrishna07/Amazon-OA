# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:14:56 2024

@author: Vamsi
"""

def getMaximumPoints(days, k):
    sprints = []
    for day in days:
        for i in range(day):
            sprints.append(i+1)
    n, start, end, res = len(sprints), 0, k-1, float('-inf')
    curr = sum( sprints[start:end+1])
    while end <= n:
        res = max( res, curr )
        curr -= sprints[start]
        start += 1
        end += 1
        if end < n:
            curr += sprints[end]
    
    return res
    

days = [ 2, 3, 2 ]
k = 4

res = getMaximumPoints(days, k)
print( res )
