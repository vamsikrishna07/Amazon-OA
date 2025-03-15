# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:21:49 2024

@author: Vamsi
"""

def next_special_string(s):
    n = len(s)
    s = list(s)
    
    # First, check for any repeated characters
    for i in range(1, n):
        if s[i] == s[i - 1]:
            # Try to change the repeated character
            for next_char in range(ord(s[i]) + 1, ord('z') + 1):
                if chr(next_char) != s[i - 1]:
                    s[i] = chr(next_char)
                    # Fill the rest of the string with the smallest possible valid characters
                    for j in range(i + 1, n):
                        for c in range(ord('a'), ord('z') + 1):
                            if chr(c) != s[j - 1]:
                                s[j] = chr(c)
                                break
                    return ''.join(s)
            # If it's 'z' and can't be incremented, return -1
            return '-1'
    
    # If no repeated characters are found, handle the non-repeated case
    for i in range(n - 1, -1, -1):
        for next_char in range(ord(s[i]) + 1, ord('z') + 1):
            if (i == 0 or chr(next_char) != s[i - 1]):
                s[i] = chr(next_char)
                # Fill the rest of the string with the smallest possible valid characters
                for j in range(i + 1, n):
                    for c in range(ord('a'), ord('z') + 1):
                        if chr(c) != s[j - 1]:
                            s[j] = chr(c)
                            break
                return ''.join(s)
    
    return '-1'


# Test cases

s = 'abcdefghz'
res = next_special_string(s)

print(res)
