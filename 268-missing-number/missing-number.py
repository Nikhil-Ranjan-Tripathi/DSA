class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i

        return max(nums)+1