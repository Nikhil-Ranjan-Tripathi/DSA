class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        j = sum(nums)
        s = 0
        mini = min(nums)
        a = 0

        
        
        for i in range(len(nums)):
            s+=nums[i]
            mini = max(mini, s)
            if s<0:
                s=0
            a = mini

        mini = min(nums)
        s=0

        for i in range(len(nums)):
            s+=nums[i]
            if s>0:
                s=0
            else:
                mini = min(mini, s)

        if a<0:
            return a
        

        return max(a,j-mini)
