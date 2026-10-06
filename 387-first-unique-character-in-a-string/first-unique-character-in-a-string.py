from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(list(s))
        for k in range(len(s)):
            if c[s[k]]==1:
                return k

        return -1