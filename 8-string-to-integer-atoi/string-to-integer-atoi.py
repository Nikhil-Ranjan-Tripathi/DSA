class Solution:
    def myAtoi(self, s: str) -> int:
        n = 0
        a = ''
        s = s.strip()
        num = 0
        for i in range(len(s)):
            if s[i].isdigit() or ((s[i]=='-' or s[i]=='+') and i==0):
                a+=s[i]
            else:
                break

        for i in range(len(a)):
            if a[i].isdigit():
                num=num*10+int(a[i])
        
        if len(a)>0 and a[0]=='-':
            return max(-num, -2147483648)
        
        return min(num, 2147483647)