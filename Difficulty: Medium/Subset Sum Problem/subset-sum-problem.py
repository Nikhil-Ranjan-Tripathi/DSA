class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        dp = [False] * (sum + 1)
        dp[0] = True

        for num in arr:
            for s in range(sum, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
                
        return dp[sum]