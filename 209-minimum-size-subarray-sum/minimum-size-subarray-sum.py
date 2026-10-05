# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # j = 0
        # s = 0
        # k = 0
        # p = sum(nums)
        # if p<target:
        #     return 0

        # for i in range(len(nums)):
        #     s += nums[i]
        #     k+=1
        #     while s>=target: 
        #         p = min(p, k)
        #         s-=nums[j]
        #         j+=1
        #         k-=1
        #         if s>=target:
        #             p = min(p, k)

        # return p       
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans