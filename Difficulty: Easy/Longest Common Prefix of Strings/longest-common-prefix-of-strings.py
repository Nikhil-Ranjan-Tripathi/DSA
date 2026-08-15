class Solution:
    def longestCommonPrefix(self, arr):
        a = ''
        b = arr[0]
        for i in range(len(arr)):
            j=0
            while j<len(b) and j<len(arr[i]):
                if b[j]!=arr[i][j]:
                    break
                j+=1
                
            b = b[:j]
                
            if b[:j]=="":
                return ""
                
        return b