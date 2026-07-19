from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        a = '$'
        c = Counter(s)
        
        for k, v in c.items():
            if v==1:
                return k
                
        
        return a