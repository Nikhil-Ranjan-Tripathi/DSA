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