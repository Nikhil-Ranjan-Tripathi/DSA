class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = min(nums)
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            maxi = max(maxi, s)
            if s<0:
                s = 0

        return maxi