class Solution:
    def product(self, arr):
        
        def solve(n):
            if n==len(arr):
                return 1
                
            return arr[n]*solve(n+1)
            
        return solve(0)%1000000007