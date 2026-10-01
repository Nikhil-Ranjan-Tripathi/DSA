class Solution:
    def countSubstrings(self, s: str) -> int:
        j = 0
        maxi = 0

        for i in range(len(s)):
            a = s[i]
            for j in range(i, len(s)):
                if j==i:
                    maxi+=1
                else:
                    a+=s[j]
                    if a==a[::-1]:
                        maxi+=1

        return maxi