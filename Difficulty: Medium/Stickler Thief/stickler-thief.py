class Solution:  
    def findMaxSum(self, arr):
        n = len(arr)
        if n==1:
            return arr[0]
            
        d = [0]*n
        d[0] = arr[0]
        d[1] = max(arr[1], arr[0])
        
        for i in range(2, len(arr)):
            d[i] = max(d[i-1], d[i-2]+arr[i])
            
        return d[-1]
                
                