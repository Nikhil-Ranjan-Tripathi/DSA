class Solution:
    def productExceptSelf(self, arr):
        # code here
        res = [1]*len(arr)
        
        l = 1
        for i in range(len(arr)):
            res[i] = l
            l*=arr[i]
        
        r = 1
        for i in range(len(arr)-1,-1,-1):
            res[i]*=r
            r*=arr[i]
            
        return res