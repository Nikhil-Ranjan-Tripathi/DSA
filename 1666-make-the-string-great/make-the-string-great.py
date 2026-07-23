class Solution:
    def makeGood(self, s: str) -> str:
        a = []
        for i in s:
            if a and a[-1] == i:
                a.append(i) 
            elif a and (a[-1].upper()==i or a[-1]==i.upper()):
                a.pop()
            else:
                a.append(i)

        return ''.join(a)