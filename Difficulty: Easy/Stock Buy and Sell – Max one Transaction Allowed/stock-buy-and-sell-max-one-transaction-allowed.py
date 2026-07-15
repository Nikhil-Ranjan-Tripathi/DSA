class Solution:
    def maxProfit(self, p):
        # code here
        suff = []
        maxi = 0
        for i in range(len(p)-1, -1, -1):
            maxi = max(maxi, p[i])
            suff.append(maxi)
        maxi = 0
        suff = suff[::-1]
        for i in range(len(p)-1):
            diff = suff[i]-p[i]
            maxi = max(maxi, diff)
            
        return maxi