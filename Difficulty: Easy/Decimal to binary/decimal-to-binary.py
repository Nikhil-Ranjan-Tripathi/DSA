class Solution:
    def decToBinary(self, n):
        l = []
        
        def solve(n):
            if n==0:
                return
            l.append(str(n%2))
            solve(int(n//2))
            
        solve(n)
        l = l[::-1]
        return int(''.join(l))