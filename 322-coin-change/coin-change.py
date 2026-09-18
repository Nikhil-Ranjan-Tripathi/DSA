class Solution:
    def coinChange(self, nums: list[int], amount: int) -> int:
        nums.sort(reverse=True)

        dp = {}

        def solve(i, left):

            if left == 0:
                return 0

            if i >= len(nums):
                return float('inf')

            if (i, left) in dp:
                return dp[(i, left)]

            if nums[i] > left:
                dp[(i, left)] = solve(i + 1, left)
                return dp[(i, left)]

            take = 1 + solve(i, left - nums[i])
            skip = solve(i + 1, left)

            dp[(i, left)] = min(take, skip)

            return dp[(i, left)]

        result = solve(0, amount)

        if result == float('inf'):
            return -1

        return result