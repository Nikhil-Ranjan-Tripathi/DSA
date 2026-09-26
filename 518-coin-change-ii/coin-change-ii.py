class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memo = {}

        def solve(i, s):
            if s==amount:
                return 1
            if s>amount or i>=len(coins):
                return 0

            if (i, s) in memo:
                return memo[(i, s)]

            p = solve(i, s+coins[i])
            n = solve(i+1, s)

            memo[(i, s)] = p+n

            return memo[(i,s)]

        return solve(0,0)
            