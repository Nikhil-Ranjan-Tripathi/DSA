class Solution:
    def deleteMid(self, s):
        if len(s)//2==0:
            return 0
        s.pop((len(s)-1)//2)