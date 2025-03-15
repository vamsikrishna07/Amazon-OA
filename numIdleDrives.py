# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:18:46 2024

@author: Vamsi
"""

from collections import defaultdict
from bisect import bisect_left, bisect_right

def numIdleDrives(x, y):
    n = len(x)
    xm = defaultdict(list)
    ym = defaultdict(list)
    
    for i in range(n):
        xm[y[i]].append(x[i])
        ym[x[i]].append(y[i])
    
    for key in xm:
        xm[key].sort()
    
    for key in ym:
        ym[key].sort()
    
    count = 0
    for i in range(n):
        cx, cy = x[i], y[i]
        r = xm[cy]
        s = ym[cx]
        
        above = bisect_right(r, cx) < len(r)
        below = bisect_left(r, cx) > 0
        left = bisect_right(s, cy) < len(s)
        right = bisect_left(s, cy) > 0
        
        if above and below and left and right:
            count += 1
    
    return count


x = [ 0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1 ]
y = [ -1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0 ]

res = numIdleDrives(x, y)

print( res )

