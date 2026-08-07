class Solution:
    def search(self, arr, x):
        def solve(n):
            if n==len(arr):
                return -1
                
            if arr[n]==x:
                return n
            else:
                return solve(n+1)
                
        return solve(0)