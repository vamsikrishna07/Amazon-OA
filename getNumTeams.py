# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:53:25 2024

@author: Vamsi
"""
def getNumTeams(skills, min_skill, max_skill):
    skills.sort()
    left = 0
    right = len(skills) - 1
    count = 0

    while left < right:
        current_sum = skills[left] + skills[right]
        
        if current_sum < min_skill:
            left += 1  # Increase the sum by moving the left pointer to the right
        elif current_sum >  8u max_skill:
            right -= 1  # Decrease the sum by moving the right pointer to the left
        else:
            # All pairs (left, left+1, ..., right-1) with skill[right] will have a valid sum
            count += (right - left)
            left += 1  # Move left pointer to explore other possibilities
    
    return count

skills = [ 2, 3, 8, 7, 5, 4, 1, 2 ] 
min_skill = 5
max_skill = 7

teams = getNumTeams(skills, min_skill, max_skill)

print( teams )