class Solution:
    def isHappy(self, n: int) -> bool:
        s = []

        while n!=1:
            s.append(n)
            l = list(str(n))
            n = 0
            for i in l:
                n+= int(i)**2
            if n in s:
                return False
            s.append(n)
        return True