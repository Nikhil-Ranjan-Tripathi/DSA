class Solution(object):
    def maximumSubarraySum(self, nums, k):
        maxi = 0
        s = 0
        d = {}
        for i in range(k):
            s += nums[i]
            d[nums[i]] = d.get(nums[i], 0) + 1
        if len(d) == k:
            maxi = s
        for i in range(k, len(nums)):
            left = nums[i-k]
            s -= left
            d[left] -= 1
            if d[left] == 0:
                del d[left]
            s += nums[i]
            d[nums[i]] = d.get(nums[i], 0) + 1
            if len(d) == k:
                maxi = max(maxi, s)

        return maxi


