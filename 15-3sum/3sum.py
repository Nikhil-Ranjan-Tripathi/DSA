class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        target = 0
        for i in range(len(nums)-2):
            s_a = []
            a = target - nums[i]
            s = {}
            for j in range(i+1, len(nums)):
                b = a - nums[j]

                if b in s:
                    ans.add((nums[i], b, nums[j]))
                    s_a = []
                s[nums[j]] = j

        return [list(x) for x in ans]




        