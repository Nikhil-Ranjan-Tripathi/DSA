class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d ={0:-1}
        pre = 0

        for i in range(len(nums)):
            pre+=nums[i]
            rem = pre%k
            if rem in d:
                if i - d[rem]>=2:
                    return True
            else:
                d[rem] = i
        
        return False
