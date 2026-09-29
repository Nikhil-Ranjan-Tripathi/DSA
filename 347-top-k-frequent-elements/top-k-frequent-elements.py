from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        a = []
        c = dict(sorted(c.items(), key = lambda item:item[1], reverse=True))
        for ke, v in c.items():
            a.append(ke)
        
        return a[:k]