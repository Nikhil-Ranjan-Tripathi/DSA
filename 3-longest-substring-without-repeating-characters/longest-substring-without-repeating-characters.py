class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        w = ''
        m = 0
        for i in range(len(s)):
            w+=s[i]
            if len(set(w)) == len(w):
                m = max(m, len(w))
            else:
                while len(set(w)) < len(w):
                    w = w[j+1:]

        return m

