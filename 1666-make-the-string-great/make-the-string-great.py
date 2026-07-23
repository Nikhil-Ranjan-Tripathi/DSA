class Solution:
    def makeGood(self, s: str) -> str:
        a = []
        for i in s:
            if a and (a[-1].upper()==i.upper()) and a[-1]!=i:
                a.pop()
            else:
                a.append(i)

        return ''.join(a)