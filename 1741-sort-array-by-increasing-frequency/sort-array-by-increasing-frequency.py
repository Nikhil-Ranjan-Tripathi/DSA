from collections import Counter
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        c = dict(sorted(c.items(), reverse = True))
        c = dict(sorted(c.items(), key = lambda item:item[1]))
        l = []
        for k, v in c.items():
            for i in range(v):
                l.append(k)

        return l
        