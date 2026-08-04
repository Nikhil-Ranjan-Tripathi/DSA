class Solution:
    def countDigits(self, n: int) -> int:
        m = n
        c = 0

        while n>0:
            a = n%10
            if m%a==0:
                c+=1
            n//=10

        return c