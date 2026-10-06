class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if 0 not in nums:
            return 0
        n = max(nums)
        s = n*(n+1)/2
        return n+1 if s==sum(nums) else int(s-sum(nums))