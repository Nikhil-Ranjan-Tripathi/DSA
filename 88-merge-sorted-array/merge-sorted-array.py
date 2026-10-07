class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = m+n
        for i in range(m, len(nums1)):
            nums1[i]=nums2[i-n]
        nums1.sort()

