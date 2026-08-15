class Solution:
	def addBinary(self, s1, s2):
		x = int(str(s1), 2)
		y = int(str(s2), 2)
		
		return bin(x+y)[2:]