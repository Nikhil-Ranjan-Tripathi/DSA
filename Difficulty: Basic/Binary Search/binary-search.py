class Solution:
    def binarySearch(self, arr, k):
        i = 0
        j = len(arr)-1
        
        def solve(i, j):
            if i>j:
                return False
                
            mid = (i+j)//2
            
            if arr[mid]==k:
                return True
            elif arr[mid]>k:
                return solve(i, j-1)
            else:
                return solve(i+1, j)
                
        return solve(i, j)