class Solution:
    def trap(self, h: List[int]) -> int:
        pre = [h[0]]
        suf = [0]*len(h)
        suf[-1] = h[-1]
        w=0
        for i in range(1, len(h)):
            pre.append(max(pre[i-1], h[i]))
        
        for i in range(len(h) - 2, -1, -1):
            suf[i] = max(suf[i + 1], h[i])
        
        for i in range(len(h)):
            if h[i]<pre[i] and h[i]<suf[i]:
                w+=min(pre[i], suf[i])-h[i]

        return w