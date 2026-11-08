from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # c = Counter(nums)
        # a = []
        # c = dict(sorted(c.items(), key = lambda item:item[1], reverse=True))
        # for ke, v in c.items():
        #     a.append(ke)
        
        # return a[:k]

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        buckets = buckets[::-1]
        for l in buckets:
            result = result+l
        
        return result[:k]