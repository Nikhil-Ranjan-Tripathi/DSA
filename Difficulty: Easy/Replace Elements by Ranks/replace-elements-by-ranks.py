from collections import defaultdict, deque
class Solution:
    def replaceWithRank(self, arr):
        # Sort including duplicates
        sorted_arr = sorted(arr)

        # Store all ranks for each value
        ranks = defaultdict(deque)

        for i, num in enumerate(sorted_arr, 1):
            ranks[num].append(i)
            
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]].popleft()-1
            
            
                
        
            
        
        
        
        
                
        
        