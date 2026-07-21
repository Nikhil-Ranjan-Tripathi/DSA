class Solution:
    def isPalindrome(self, n):
        a = abs(n)
		l = list(str(a))
		return l==l[::-1]
		
		