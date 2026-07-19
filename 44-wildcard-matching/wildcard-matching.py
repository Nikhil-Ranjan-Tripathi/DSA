class Solution:
    def isMatch(self, pattern: str, wild: str) -> bool:
        n, m = len(wild), len(pattern)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if wild[i-1] == '*':
                dp[i][0] = dp[i-1][0]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if wild[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif wild[i-1] == '?' or wild[i-1] == pattern[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        
        return True if dp[n][m] else False