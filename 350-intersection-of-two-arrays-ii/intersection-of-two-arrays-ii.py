from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = Counter(nums1)
        result = []
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result   
        
        # for single elemets only
        # return list(set(nums1) & set(nums2))