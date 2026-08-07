class Solution:
    def getSecondLargest(self, arr):
        a = max(arr)
        def solve(n):
            if n==len(arr):
                return
            
            if arr[n]==a:
                arr[n]=-1
                
            solve(n+1)
            
        solve(0)
        
        return max(arr)
        