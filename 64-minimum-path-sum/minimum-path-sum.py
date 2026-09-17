class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[0][i] = grid[0][i]+dp[0][i-1]

        for i in range(1, m):
            dp[i][0] = grid[i][0]+dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        
        #initial states
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1] + grid[0][i]
        

        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
        
"""

"""
def solve(grid):
    m = len(grid)
    n = len(grid[0])
    
    def is_safe(a, b):
        return (0<=a<m and 0<=b<n)
    
    def solving(a, b, total):
        
        if not is_safe(a, b):
            return float('inf')
            
        total+=grid[a][b]
        
        if a==m-1 and b==n-1:
            return total
        
        return min(solving(a+1, b, total), solving(a, b+1, total))
    
    return solving(0,0, 0)
"""
