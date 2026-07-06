class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        p = 0
        t = 0
        for i in nums:
            p+=i
            rem = p%k
            if rem in d:
                t+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1

        return t