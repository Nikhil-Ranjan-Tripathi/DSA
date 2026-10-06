class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # if min(nums)>1:
        #     return 1
        # for i in range(1, max(nums)):
        #     if i not in nums:
        #         return i

        # return max(nums)+1 if max(nums)>0 else 1
        nums.sort()
        expected = 1

        for num in nums:
            if num == expected:
                expected += 1
            elif num > expected:
                return expected

        return expected