class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[-1] * n for _ in range(m)]

        def solve(a, b):
            if a >= m or b >= n or grid[a][b] == 1:
                return 0

            if a == m - 1 and b == n - 1:
                return 1

            if dp[a][b] != -1:
                return dp[a][b]

            dp[a][b] = solve(a + 1, b) + solve(a, b + 1)

            return dp[a][b]

        return solve(0, 0)