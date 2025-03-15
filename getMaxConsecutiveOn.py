# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 23:00:47 2024

@author: Vamsi
"""

def getMaxConsecutiveON( server, k ):
    res, i, j, n = 0, 0, 0, len(server)

    while i < n:
        if server[i] == '1':
            while i + 1 < n and server[i + 1] == '1':
                i += 1
        elif server[i] == '0':
            while i + 1 < n and server[i + 1] == '0':
                i += 1
            k -= 1

        if k < 0:
            while server[j] == '1':
                j += 1
            if server[j] == '0':
                while server[j] == '0':
                    j += 1
                k += 1

        res = max(res, i - j + 1)
        i += 1

    return res
    return res


server =  "11101010110011"
k = 2

result = getMaxConsecutiveON( server, k )

print( result )