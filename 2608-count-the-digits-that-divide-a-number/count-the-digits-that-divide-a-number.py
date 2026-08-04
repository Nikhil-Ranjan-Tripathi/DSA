class Solution:
    def countDigits(self, n: int) -> int:
        og = n
        def solve(n):
            if n==0:
                return 0
            else:
                if n%10!=0 and og%(n%10)==0:
                    return 1+solve(n//10)
                else:
                    return solve(n//10)

        return solve(n)

            

