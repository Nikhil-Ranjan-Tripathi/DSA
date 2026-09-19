class Solution:
	def perfectSum(self, arr, target):
		# code here
		memo = {}
		
		def solve(i, left):
		    if i==len(arr):
		        if left==0:
		            return 1
		        return 0
		        
		    if (i, left) in memo:
		        return memo[(i,left)]
		        
		    skip = solve(i+1, left)
		    take = 0
		    if arr[i]<=left:
		        take = solve(i+1, left-arr[i])
		    
		    memo[(i, left)] = take + skip
		    
		    return memo[(i, left)]
		    
		   
		return solve(0, target)