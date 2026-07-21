class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n ==0:
            return 0
        elif n==1:
            return 1
        nex = 0
        for i in range(2, n+1):
            nex = a+b
            a = b
            b = nex

        return nex            