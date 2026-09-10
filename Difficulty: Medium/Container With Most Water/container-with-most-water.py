class Solution:
    def maxWater(self, arr):
        p = 0
        i=0
        j=len(arr)-1
        while i<j:
            water = min(arr[i], arr[j])*(j-i)
            p = max(p, water)
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
        return p