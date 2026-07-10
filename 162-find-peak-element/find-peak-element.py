class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        m = max(nums)

        for i in range(len(nums)):
            if nums[i]==m:
                return i