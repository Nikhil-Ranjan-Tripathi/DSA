class Solution:
    def missingNum(self, arr):
        # code here
        l = len(arr)+1
        s = l*(l+1)/2
        s1 = sum(arr)
        return int(s-s1)