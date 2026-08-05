class Solution:
    def isSorted(self, arr):
        
        def solve(n):
            if n+1==len(arr):
                return True
            if arr[n]>arr[n+1]:
                return False
            else:
                return solve(n+1)
            
        return solve(0)