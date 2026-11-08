class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxR = 0

        for i in range(len(nums)):
            if i > maxR:
                return False

            maxR = max(maxR, i+nums[i])

            if maxR>len(nums)-1:
                return True

        return True