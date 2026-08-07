class Solution:
    def countZeroes(self, arr):
        def solve(n):
            if n==len(arr):
                return 0
                
            if arr[n]==0:
                return 1+ solve(n+1)
            return solve(n+1)
            
        return solve(0)
        
        