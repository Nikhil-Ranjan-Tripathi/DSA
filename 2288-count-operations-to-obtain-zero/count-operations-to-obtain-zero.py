class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        def solve(n, m):
            if n==0 or m==0:
                return 0
            if n==m:
                return 1
            if n>m:
                return 1+ solve(n-m, m)
            if n<m:
                return 1+solve(n, m-n)

        return solve(num1, num2)