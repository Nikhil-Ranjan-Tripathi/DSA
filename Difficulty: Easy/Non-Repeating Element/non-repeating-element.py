from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        c = Counter(arr)
        for k, v in c.items():
            if v==1:
                return k
                
        return 0
                
        