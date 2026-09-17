class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        memo={}
        def recursion(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=n or j>=m:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==n-1 and j==m-1:
                return 1
              
            bottom=recursion(i+1,j)
            right=recursion(i,j+1)
            memo[(i,j)]=bottom+right
            return memo[(i,j)]
        return recursion(0,0)
