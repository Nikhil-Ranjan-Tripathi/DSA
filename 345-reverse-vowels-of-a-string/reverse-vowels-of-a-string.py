class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i2 = []
        v = ['a', 'e', 'i', 'o', 'u']
        v2 = []
        for i in range(len(s)):
            if s[i].lower() in v:
                v2.append(s[i])
                i2.append(i)

        v2 = v2[::-1]

        for i in range(len(i2)):
            s[i2[i]] = v2[i]

        return "".join(s)