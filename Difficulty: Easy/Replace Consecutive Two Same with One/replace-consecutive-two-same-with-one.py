class Solution:
    def removeDuplicates(self, s):
        if not s:
            return ""
        ans = [s[0]]
        def solve(i):
            if i == len(s):
                return
            if s[i] != ans[-1]:
                ans.append(s[i])
            solve(i + 1)
        solve(1)

        return "".join(ans)

"""
class Solution:
    def removeDuplicates(self, s):
        ans = s[0]
        def solve(n, ans):
            if n==len(s):
                return ans
            
            if s[n]!=ans[-1]:
                ans+=s[n]
            return solve(n+1, ans)
                
        
        return solve(1, ans)
"""
