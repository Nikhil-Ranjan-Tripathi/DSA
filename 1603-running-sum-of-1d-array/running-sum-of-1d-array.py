class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # l = []
        # s = 0
        # def solve(n, s, l):
        #     if n==len(nums):
        #         return
            
        #     else:
        #         s+=nums[n]
        #         l.append(s)
        #         return solve(n+1, s, l)

        # solve(0, 0, l)

        # return l
        a = 0
        for i in range(len(nums)):
            c = nums[i]
            nums[i] += a
            a = a + c

        return nums 

