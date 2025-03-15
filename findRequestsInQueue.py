# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 19:27:58 2024

@author: Vamsi
"""

from collections import defaultdict
def findRequestsInQueue(wait):
    results = []
    counter = defaultdict(int)
    
    # init counter
    for x in wait:
        counter[x] += 1
    
    # iterate queue
    t = 0
    qlen = len(wait)
    for x in wait:
        if x <= t:
            continue
        results.append(qlen)
        counter[x] -= 1
        t += 1
        qlen = qlen - counter[t]
        qlen -= 1
    return results + [0]

wait = [3,1,2,1]
print(findRequestsInQueue(wait)) 

