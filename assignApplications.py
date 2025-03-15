# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:50:04 2024

@author: Vamsi
"""
import bisect

def assignApplications(memory_capacity, foreground, background):
    # Step 1: Sort both lists by memory usage
    foreground.sort(key=lambda x: x[1])
    background.sort(key=lambda x: x[1])
    
    # Extract background memory values and IDs for easy access
    bg_memories = [mem for _, mem in background]
    bg_ids = [id for id, _ in background]
    
    max_memory = -1
    result = []
    
    # Step 2: Iterate through the foreground list
    for fg_id, fg_mem in foreground:
        # Calculate the maximum memory we can use from background
        complement = memory_capacity - fg_mem
        
        # Step 3: Binary search for the largest valid memory in the background list
        idx = bisect.bisect_right(bg_memories, complement)
        
        if idx > 0:
            idx -= 1
            bg_id = bg_ids[idx]
            bg_mem = bg_memories[idx]
            current_memory = fg_mem + bg_mem
            
            if current_memory <= memory_capacity:
                if current_memory > max_memory:
                    max_memory = current_memory
                    result = [(fg_id, bg_id)]
                elif current_memory == max_memory:
                    result.append((fg_id, bg_id))
                    
            while idx > 0 and bg_memories[idx - 1] == bg_memories[idx]:
                idx -= 1
                bg_id = bg_ids[idx]
                bg_mem = bg_memories[idx]
                current_memory = fg_mem + bg_mem
                
                if current_memory <= memory_capacity:
                    if current_memory > max_memory:
                        max_memory = current_memory
                        result = [(fg_id, bg_id)]
                    elif current_memory == max_memory:
                        result.append((fg_id, bg_id))
                        
    return result

# Example usage:
memory_capacity = 10
foreground = [(2, 1), (3, 4), (1, 5), (0, 9)]
background = [(1, 2), (3, 3), (2, 3), (0, 7), (4, 10)]

result = assignApplications(memory_capacity, foreground, background)
print(result)
