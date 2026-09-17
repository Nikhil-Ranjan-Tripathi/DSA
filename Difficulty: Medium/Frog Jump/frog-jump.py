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
"""
class Solution:
    def minCost(self, height: list[int]) -> int:
        if len(height)<2:
            return 0
        
        def solve(i, j):
            if j>=len(height):
                return float('inf')
            cost = abs(height[j]-height[i])
            if j==len(height)-1:
                return cost
            return cost+min(solve(j,j+1), solve(j,j+2))
        return min(solve(0, 1), solve(0,2))
"""
