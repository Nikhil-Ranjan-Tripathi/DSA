from collections import Counter
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = list(set(nums1))+list(set(nums2))
        nums1.sort()
        c = Counter(nums1)
        a = []
        for k, v in c.items():
            if v==2:
                a.append(k)

        return a

