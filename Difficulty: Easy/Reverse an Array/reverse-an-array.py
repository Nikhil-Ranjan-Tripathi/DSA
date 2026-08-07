class Solution:
    def reverseArray(self, arr):
        
        def rev(l, r):
            if l>=r:
                return arr[r]
                
            arr[l], arr[r] = arr[r], arr[l]
            
            rev(l+1, r-1)
        rev(0, len(arr)-1)
        
        return arr