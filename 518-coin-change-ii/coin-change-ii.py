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
            

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount+1)
#         dp[0] = 1
#         for n in coins:
#             for i in range(len(dp)-n):
#                 if dp[i]:
#                     dp[i+n] += dp[i]
#         return dp[-1]