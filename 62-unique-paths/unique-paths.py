class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def solve(r,c):
            if r>=m or c>=n:
                return 0
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = solve(r+1, c)+solve(r,c+1)
            return memo[(r,c)]
        return solve(0,0)