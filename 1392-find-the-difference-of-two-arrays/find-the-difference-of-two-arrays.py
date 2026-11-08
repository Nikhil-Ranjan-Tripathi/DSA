class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        l = [[], []]
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                l[0].append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                l[1].append(nums2[i])

        return l