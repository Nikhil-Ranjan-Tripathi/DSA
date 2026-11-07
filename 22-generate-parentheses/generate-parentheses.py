class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n==1:
            return ["()"]
        result = []
        curr = []
        def back(open, close):
            if open == n and close == n:
                result.append("".join(curr))
                return
            
            if open<n:
                curr.append("(")
                back(open+1, close)
                curr.pop()

            if close<open:
                curr.append(")")
                back(open, close+1)
                curr.pop()

        back(0, 0)

        return result

