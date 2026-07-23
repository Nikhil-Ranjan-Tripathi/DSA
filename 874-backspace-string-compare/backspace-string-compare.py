class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        for i in range(len(s)):
            if s[i]=='#':
                if len(a)>0:
                    a.pop()
            else:
                a.append(s[i])

        for i in range(len(t)):
            if t[i]=='#':
                if len(b)>0:
                    b.pop()
            else:
                b.append(t[i])

        if a==b:
            return True
        return False