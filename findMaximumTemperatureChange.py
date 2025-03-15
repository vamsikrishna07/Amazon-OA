# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:55:45 2024

@author: Vamsi
"""

def findMaximumChange( temperatureChange ):
    n, res = len( temperatureChange ), float( '-inf' )
    prefix, suffix = [0]*n , [0]*n
    prefix[0] = temperatureChange[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + temperatureChange[i]
    suffix[-1] = temperatureChange[-1]
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] + temperatureChange[i]
    for i in range(n):
        res = max( res, max(prefix[i], suffix[i]) )
    return res
    
temperatureChange = [ 6, -2, 5 ]
res = findMaximumChange( temperatureChange )

print( res )