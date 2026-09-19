class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        dp = [False] * (sum + 1)
        dp[0] = True

        for num in arr:
            for s in range(sum, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
                
        return dp[sum]

"""
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        memo = {}
        
        def solve(i, left):
            if left==0:
                return True
            
            if i>=len(arr) or left<0:
                return False
            
            if (i,left) in memo:
                return memo[(i,left)]
                
            take = solve(i+1, left-arr[i])
            skip = solve(i+1, left)
            
            memo[(i,left)] = take or skip
            
            return memo[(i, left)]
            
        return solve(0, sum)
"""
