class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        j = 0
        for i in range(len(s2)):
            if j<len(s1):
                if s2[i] == s1[j]:
                    j+=1
            
        if j==len(s1):
            return True
        return False
            
            