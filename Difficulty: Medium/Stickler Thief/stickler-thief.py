class Solution:  
    def findMaxSum(self, arr):
        # code here
        memo = {}
        def solve(i):
            if i>=len(arr):
                return 0
            if i in memo:
                return memo[i]
                
            memo[i] = arr[i] + max(solve(i+2), solve(i+3))
            return memo[i]
        
        return max(solve(0), solve(1))