class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = []
        for i in range(len(s)):
            if len(a)>0:
                if s[i] == a[-1]:
                    a.pop()
                else:
                    a.append(s[i])
            else:
                a.append(s[i])

        return ''.join(a)