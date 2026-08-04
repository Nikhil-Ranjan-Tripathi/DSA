class Solution:
    def reverseString(self, s: str) -> str:
        def solve(n):
            if n==0:
                return s[0]
                
            return s[n]+solve(n-1)
            
        return solve(len(s)-1)