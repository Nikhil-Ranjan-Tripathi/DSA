class Solution:
    def minCost(self, height: list[int]) -> int:

        n = len(height)

        if n < 2:
            return 0

        dp = [0] * n

        for i in range(1, n):

            one = dp[i-1] + abs(height[i] - height[i-1])

            two = float('inf')

            if i >= 2:
                two = dp[i-2] + abs(height[i] - height[i-2])

            dp[i] = min(one, two)

        return dp[n-1]