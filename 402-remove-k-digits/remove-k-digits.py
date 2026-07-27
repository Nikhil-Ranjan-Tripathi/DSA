class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        l = []

        for n in s:
            while l and k and l[-1]>n:
                l.pop()
                k-=1

            if l or n is not '0':
                l.append(n)

        if k:
            l = l[:-k]
        return ''.join(l) or "0"