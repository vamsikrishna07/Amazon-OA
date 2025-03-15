# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:10:13 2024

@author: Vamsi
"""

def splitPrefixSuffix( categories, k ):
    n, res = len(categories), 0
    count_prefix, count_suffix, prefix_set, suffix_set = [0]*n, [0]*n, set(), set()
    for i in range(n):
        prefix_set.add(categories[i])
        count_prefix[i] = len(prefix_set)
    for i in range(n-1,-1,-1):
        suffix_set.add(categories[i])
        count_suffix[i] = len(suffix_set)
    for i in range(n-1):
        if count_prefix[i]>k and count_suffix[i+1]>k:
            res += 1
    return res

categories = 'wxyxxyxw'
k = 1
res = splitPrefixSuffix(categories, k)
print( res )