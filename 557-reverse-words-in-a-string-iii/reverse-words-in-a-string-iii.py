class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)):
            a = l[i][::-1]
            l[i] = a

        return " ".join(l)