from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:

        c = Counter(s)

        el = []
        ol = []

        for k, v in c.items():
            if v % 2 == 0:
                el.append(v)
            else:
                ol.append(v - 1)

        a = 0

        if len(ol) > 0:
            a = 1

        return sum(el) + sum(ol) + a