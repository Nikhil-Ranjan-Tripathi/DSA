class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a % b)

""" 
class Solution:
    def gcd(self, a, b):
        if a==0 or b==0:
            return min(a, b)
            
        if a>=b:
            if a%b==0:
                return b
            return self.gcd(a-b, b)
        if b>a:
            if b%a==0:
                return a
            return self.gcd(a, b-a)
            
                
"""
