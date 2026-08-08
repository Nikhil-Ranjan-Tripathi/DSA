class Solution:
    def numberOfPaths(self, m, n):
        dp = {}

        def solve(m, n):
            if m == 1 or n == 1:
                return 1

            if (m, n) in dp:
                return dp[(m, n)]

            dp[(m, n)] = solve(m - 1, n) + solve(m, n - 1)

            return dp[(m, n)]

        return solve(m, n)