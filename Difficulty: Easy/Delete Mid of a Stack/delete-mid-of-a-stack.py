class Solution:
    def deleteMid(self, s):
        if len(s)//2==0:
            return 0
        s.pop((len(s)-1)//2)

"""
class Solution:
    def deleteMid(self, s):
        def solve(k):
            if k == 0:
                s.pop()
                return

            x = s.pop()
            solve(k - 1)
            s.append(x)

        solve(len(s) // 2)
"""
