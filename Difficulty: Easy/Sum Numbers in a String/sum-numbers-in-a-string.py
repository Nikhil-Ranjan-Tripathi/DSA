class Solution:
    def findSum(self, s):
        a = 0
        b = 0
        for i in s:
            if i.isdigit():
                a = a*10+int(i)
            else:
                b+=a
                a = 0
        b+=a
        return b