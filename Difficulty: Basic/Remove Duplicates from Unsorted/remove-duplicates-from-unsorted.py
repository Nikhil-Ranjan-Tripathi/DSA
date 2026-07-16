class Solution:
    def removeDuplicate(self, arr):
        s = set()
        l = []
        for i in arr:
            if i not in s:
                s.add(i)
                l.append(i)
                
        return l
