class Solution:
    def getMinMax(self, arr):
        l = [10**7, 0]
        
        def solve(n, l):
            if n==len(arr):
                return
            l[0] = min(arr[n], l[0])
            l[1] = max(arr[n], l[1])
            solve(n+1, l)
            
        solve(0, l)
        
        return l
            
            