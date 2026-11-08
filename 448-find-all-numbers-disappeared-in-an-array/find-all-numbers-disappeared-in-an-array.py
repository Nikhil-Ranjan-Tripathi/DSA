class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        n = len(nums)
        nums = set(nums)
        re = []
        for i in range(1, n+1):
            if i not in nums:
                re.append(i)

        return re
