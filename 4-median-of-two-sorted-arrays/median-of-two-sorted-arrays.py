class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1+nums2
        n.sort()
        if len(n)%2==0:
            a = n[(len(n)-1)//2]+n[((len(n)-1)//2)+1]
            return (a*1.00000)/2

        else:
            return (n[(len(n)-1)//2])*1.00000