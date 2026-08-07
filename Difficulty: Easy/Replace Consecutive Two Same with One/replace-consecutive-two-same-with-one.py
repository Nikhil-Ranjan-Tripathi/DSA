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