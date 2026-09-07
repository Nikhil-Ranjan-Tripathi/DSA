class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        dp = [0]*(W+1)
        
        for i in range(n):
            for w in range(W, wt[i]-1, -1):
                dp[w] = max(dp[w],val[i]+dp[w-wt[i]])
                
        return dp[W]