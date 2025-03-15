# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:48:57 2024

@author: Vamsi
"""
# def getMissingNumber( nums ):
#     missing = len(nums)
#     for i, num in enumerate(nums):
#         missing ^= i ^ num
#     return missing

# def getRepeatingNumber( nums ):
#     for num in nums:
#         cur = abs(num)
#         if nums[cur] < 0:
#             duplicate = cur
#             break
#         nums[cur] = -nums[cur]

#     # Restore numbers
#     for i in range(len(nums)):
#         nums[i] = abs(nums[i])

#     return duplicate    

# def getRepeatingAndMissingNumber( nums ):
#     a = getRepeatingNumber(nums)
#     b = getMissingNumber(nums)
#     return [a, b]

def find_missing_and_repeated(nums):
    n = len(nums)
    
    # Step 1: XOR all the elements in the array
    xor_all_elements = 0
    for num in nums:
        xor_all_elements ^= num

    # Step 2: XOR the result with numbers from 1 to n
    xor_1_to_n = 0
    for i in range(1, n + 1):
        xor_1_to_n ^= i
    
    # XOR of missing and repeated number
    xor_result = xor_all_elements ^ xor_1_to_n
    
    # Step 3: Find the rightmost set bit in xor_result
    rightmost_set_bit = xor_result & -xor_result
    
    # Initialize variables to hold missing and repeated numbers
    missing = 0
    repeated = 0
    
    # Step 4: Divide the numbers into two groups and XOR them separately
    for num in nums:
        if num & rightmost_set_bit:
            repeated ^= num
        else:
            missing ^= num
            
    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            repeated ^= i
        else:
            missing ^= i
    
    # Step 5: Check which one is missing and which one is repeated
    if repeated in nums:
        return missing, repeated
    else:
        return repeated, missing

nums = [ 3, 1, 2, 3, 5 ]

missing, repeated = find_missing_and_repeated(nums)

print( repeated, missing )