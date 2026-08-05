class Solution:
    def gcd(self, a: int, b: int) -> list:
        if a == b:
            return a, 1, 0

        if b == 0:
            return a, 1, 0

        gcd, x1, y1 = self.gcd(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        return gcd, x, y