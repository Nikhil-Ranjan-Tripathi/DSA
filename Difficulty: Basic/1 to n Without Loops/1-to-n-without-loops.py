class Solution:
    def printTillN(self, n):
    	if n==0:
    	    return
    	else:
    	    self.printTillN(n-1)
    	    print(n, end=" ")
    	    