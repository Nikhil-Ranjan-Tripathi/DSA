class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

        target = s // 2

        # def solve(i, su):
        #     if su == target:
        #         return True

        #     if i == len(nums) or su > target:
        #         return False

        #     take = solve(i + 1, su + nums[i])
        #     skip = solve(i + 1, su)

        #     return take or skip

        # if not trying1():
        #     return solve(0, 0)
        # else:
        #     return True

"""
a = [1,2,3,5]

a.sort()

store = [a[0]]
temp = []
c = False
for i in range(len(a)):
    for j in range(len(store)):
        if store[j]+a[i]==sum(a)/2:
            print("true")
            c = True
    if c==True:
            break
        
    temp.append(store[j]+a[i])
        
    store+=temp   
    store.append(a[i]) 
"""
        
