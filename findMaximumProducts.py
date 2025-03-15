# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:47:01 2025

@author: Vamsi
"""
def findMaxProducts(arr):
    n = len(arr)
    adjusted = [arr[i] - i for i in range(n)]
        
    prev_smaller = [-1]*n
    stack = []
    print(adjusted)
    for i in range(n-1,-1,-1):
        while stack and adjusted[i] <= adjusted[stack[-1]]:
            j = stack.pop()
            prev_smaller[j] = i
        stack.append(i)
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + arr[i]
        else:
            j = prev_smaller[i]
            length = min(i - j, arr[i])
            dp[i] = (arr[i] + arr[i] - length + 1) * length // 2
            if j >= 0:
                dp[i] += dp[j]
    
    return max(dp)

def findMaxProducts1(arr):
    n = len(arr)
    dp = [0]*n
    for i in range(n):
        dp[i] = arr[i]
        for j in range(i):
            dp[i] = max(dp[i], dp[j]+min(arr[i],arr[j]+1))
    return max(dp)

def max_sum_increasing_subsequence(nums):
    if not nums:
        return 0

    stack = []
    max_sum = 0
    current_sum = 0

    for num in nums:
        # If the stack is empty or the current number is greater than the last number in the stack
        if not stack or num > stack[-1]:
            stack.append(num)
            current_sum += num
        else:
            # Reset the stack for the new increasing sequence
            max_sum = max(max_sum, current_sum)
            stack = [num]
            current_sum = num

    # Check the last sequence
    max_sum = max(max_sum, current_sum)

    return max_sum
'''
res1 = findMaxProducts([2,9,4,7,5,2])
print(res1)

res2 = findMaxProducts([2,5,6,7])
print(res2)
'''
res3 = findMaxProducts([25,26,45,22,31,47,29,47,2,25,25])
print(res3)