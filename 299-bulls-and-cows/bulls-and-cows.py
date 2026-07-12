class Solution:
    def getHint(self, s: str, g: str) -> str:
        d = {}
        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1

        for i in range(len(g)):
            if g[i] in d:
                if d[g[i]]>0:
                    b+=1
                    d[g[i]]-=1
                else:
                    del d[g[i]]

            if g[i]==s[i]:
                a+=1

        b = b-a

        ans = (f"{a}A{b}B")

        return ans


        