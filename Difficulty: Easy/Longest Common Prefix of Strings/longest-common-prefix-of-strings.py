class Solution:
    def longestCommonPrefix(self, arr):
        a = []
        n = min(arr, key=len)
        j=0
        for i in range(len(n)):
            ch = arr[0][i]
            
            for s in arr:
                if s[i]!=ch:
                    return ''.join(a)
            
            a.append(ch)
        
        return ''.join(a)