class Solution:
    def romanToInteger(self, s): 
        d = {"I": 1, "V":5, "X":10, "L":50, "M": 1000, "C":100, "D":500}
        s = s[::-1]
        c = 0
        for i in range(len(s)):
            if c==0:
                c+=d[s[i]]
            else:
                if d[s[i]]<d[s[i-1]]:
                    c-=d[s[i]]
                else:
                    c+=d[s[i]]
    
        return c
            
        