# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:39:51 2024

@author: Vamsi
"""
import bisect
def getMaximumPairs( group1, group2 ):
    res, n = 0, len(group1)
    diffs = [ group1[i]-group2[i] for i in range(n) ]
    diffs.sort()
    
    for diff in diffs:
        x = bisect.bisect_right( diffs, -diff )
        res += n-x
    return res

group1 = [ 1, 2, 3, 5, 6, 7, 7, 2, 1, 4, 6, 6 ]
group2 = [ 3, 5, 7, 3, 2, 45, 3, 5, 6, 7, 8, 2 ]

res = getMaximumPairs(group1, group2)    
    
print( res )
    
    
    
    
