class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                min_health_needed = min(dp[r + 1][c], dp[r][c + 1])
                dp[r][c] = max(1, min_health_needed - dungeon[r][c])
                
        return dp[0][0]