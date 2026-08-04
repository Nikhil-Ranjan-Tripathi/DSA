class Solution:
    def printNos(self, n):
        if n>0:
            print(n, end=" ")
            self.printNos(n-1)
        