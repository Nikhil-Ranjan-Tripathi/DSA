class Solution:
    def countDigits(self, n):
        if n==0:
            return 0
        return 1+self.countDigits(n//10)