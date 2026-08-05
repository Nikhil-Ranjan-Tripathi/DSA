class Solution:
	def arraySum(self, arr):
   		s = 0
   		
   		def solve(n):
   		    if n==0:
   		        return arr[n]
   		    return arr[n] + solve(n-1)
   		    
   		return solve(len(arr)-1)
   		
