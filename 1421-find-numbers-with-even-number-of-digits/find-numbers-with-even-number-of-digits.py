class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        a = 0

        for i in range(len(nums)):
            t = str(nums[i])
            if len(t)%2==0:
                a+=1

        return a