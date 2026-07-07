class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                a+=s[i]
        a = a.lower()
        if a==a[::-1]:
            return True

        return False