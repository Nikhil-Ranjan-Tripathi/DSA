class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: 
            return n

        p1 = 1
        p2 = 2

        for i in range(3, n+1):
            c = p1+p2
            p1 = p2
            p2 = c

        return p2
