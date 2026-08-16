class Solution:
    def thirdLargest(self,arr):
        if len(arr)<3:
            return -1
            
        m = max(arr)
        for i in range(len(arr)):
            if arr[i] == m:
                arr[i] = -1
                break
                
        m = max(arr)
        for i in range(len(arr)):
            if arr[i] == m:
                arr[i] = -1
                break
                
        return max(arr)