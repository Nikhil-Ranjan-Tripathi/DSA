class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        l = []

        for i in m:
            l+=i
        
        l.sort()

        return l[k-1]
