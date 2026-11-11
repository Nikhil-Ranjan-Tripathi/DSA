class Solution:
    def maxArea(self, h: list[int]) -> int:
        i = 0
        j = len(h)-1
        m = 0
        while i<j:
            m = max(m, min(h[i],h[j])*(j-i))
            if h[i]<=h[j]:
                i+=1
            elif h[i]>h[j]:
                j-=1

        return m

            
