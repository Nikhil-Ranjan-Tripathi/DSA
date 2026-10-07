class Solution:
    def maxArea(self, h: list[int]) -> int:
        i = 0
        j = len(h)-1
        m = 0
        while i<j:
            a = min(h[i],h[j])*(j-i)
            m = max(m, a)
            if h[i]<h[j]:
                i+=1
            elif h[i]>h[j]:
                j-=1
            else:
                i+=1

        return m

            
