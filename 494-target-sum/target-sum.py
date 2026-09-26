class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        def solve(index, current_sum):
            if index==len(nums):
                return 1 if current_sum == target else 0

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            p = solve(index+1, current_sum+nums[index])
            n = solve(index+1, current_sum - nums[index]) 

            memo[index, current_sum] = p+n

            return memo[(index, current_sum)]

        return solve(0, 0)