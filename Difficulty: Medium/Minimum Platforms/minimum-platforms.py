class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code here
        arr.sort()
        dep.sort()
        i = 0
        j=0
        plat = 0
        maxi = 0
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                plat+=1
                maxi = max(maxi, plat)
                i+=1
            else:
                plat-=1
                j+=1
        return maxi