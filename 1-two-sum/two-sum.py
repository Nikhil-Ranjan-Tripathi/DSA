class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = {}

        for i in range(len(nums)):
            com = target - nums[i]
            if com in s:
                return [s[com], i]
            s[nums[i]]=i

        