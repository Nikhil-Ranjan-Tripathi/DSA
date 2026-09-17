class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        if n==0:
            return a
        if n==1:
            return b
        if n==2:
            return c

        n-=2

        for i in range(n):
            a, b, c = b, c, a+b+c

        return c