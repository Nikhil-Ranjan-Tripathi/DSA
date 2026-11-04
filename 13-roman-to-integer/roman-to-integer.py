class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s = s[::-1]
        n = d[s[0]]
        for i in range(1, len(s)):
            if d[s[i]]>=d[s[i-1]]:
                n+=d[s[i]]
            else:
                n-=d[s[i]]

        return n 