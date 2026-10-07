class Solution:
    def mergeArrays(self, a, b):
        # code here
        n = len(a)
        for i in b:
            a.append(i)
        a.sort()
        c = a[n:]
        for i in range(len(b)):
            a.pop(-1)
        
        for i in range(len(c)):
            b[i] = c[i]
        