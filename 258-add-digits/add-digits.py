class Solution:
    def addDigits(self, num: int) -> int:
        def solve1(n):
            if n==0:
                return 0
            return n%10 + solve1(n//10)

        def solve(n):
            if n<10:
                return n
            return solve(solve1(n))

            
        return solve(num)