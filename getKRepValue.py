# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:01:14 2024

@author: Vamsi
"""

def charASCII(ch):
    return ord(ch)-ord('a')

def getKRepValue( hist, k ):
    n, res, st, c = len(hist), 0, 0, [0]*26
    for i in range(n):
        e = charASCII(hist[i])
        c[e] += 1
        while c[charASCII(hist[st])] > k or ( hist[st] != hist[i] and c[e] >= k ):
            c[charASCII(hist[st])] -= 1
            st += 1
        if max(c) >= k:
            res += st+1
    return res

hist = 'ceccca'
k = 3

res = getKRepValue( hist, k )

print( res )
