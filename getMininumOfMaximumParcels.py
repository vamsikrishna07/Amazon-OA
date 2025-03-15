# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:53:37 2024

@author: Vamsi
"""

def getMinimumOfMaxParcels( parcels, extra_parcels ):
    n, m, curr, res = len(parcels), max(parcels), 0, 0
    for each in parcels:
        curr += (m-each)
    rem = extra_parcels - curr
    if rem <= 0:
        return m
    else:
        if rem % n == 0:
            res = m + ( rem // n )
        else:
            res = m + ( rem // n )  + 1
        return res
    
parcels = [ 7, 1, 2, 4, 5, 1, 4, 9, 2 ]
extra_parcels  = 75

result = getMinimumOfMaxParcels(parcels, extra_parcels)
    
print( result )