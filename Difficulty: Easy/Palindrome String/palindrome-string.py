class Solution:
    def isPalindrome(self, s):
        def solve(n):
            if n==0:
                return s[0]
                
            return s[n]+solve(n-1)
        
        return s==solve(len(s)-1)
        
