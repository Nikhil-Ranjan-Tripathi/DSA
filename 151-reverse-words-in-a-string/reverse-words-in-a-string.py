class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        i=0
        while i<len(l):
            if l[i]=="":
                l.pop(i)
                continue
            i+=1

        l = l[::-1]

        return (" ".join(l)).strip()