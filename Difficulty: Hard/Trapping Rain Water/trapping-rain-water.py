class Solution:
    def maxWater(self, arr):
        # code here
        pre = []
        suff = []
        maxi = 0
        for i in range(len(arr)):
            maxi = max(maxi, arr[i])
            pre.append(maxi)
        maxi = 0
        for i in range(len(arr)-1, -1, -1):
            maxi = max(maxi, arr[i])
            suff.append(maxi)
        suff = suff[::-1]
        area = 0
        for i in range(len(arr)):
            if arr[i]<pre[i] and arr[i]<suff[i]:
                area+=min(pre[i], suff[i]) - arr[i]
                
        return area
            