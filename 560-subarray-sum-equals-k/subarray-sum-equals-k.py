from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1   

        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            count += freq[prefix - k]

            freq[prefix] += 1

        return count

# s = 0

# for i in range(len(a)):
#     b = 0
#     j = i
#     while j<len(a):
#         b+=a[j]
#         if b<t:
#             j+=1
#         elif b>t:
#             break
#         else:
#             s+=1
#             break 