class Solution:
    def find(self, arr, x):
        l = []
        if x not in arr:
            return [-1, -1]
        def solve(n, l):
            if n==len(arr):
                return
            if arr[n]==x:
                if len(l)<=1:
                    l.append(n)
                    l.append(n)
                else:
                    l[1] = n
                    
            return solve(n+1, l)
            
        solve(0, l)    
        
        return l
        