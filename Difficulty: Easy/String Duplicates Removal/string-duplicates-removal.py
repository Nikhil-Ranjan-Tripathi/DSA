class Solution:
	def removeDuplicates(self, s):
	    # code here
	    v = []
	    a = ''
	    for i in range(len(s)):
	        if s[i] not in v:
	            a+=s[i]
	            v.append(s[i])
	    return a