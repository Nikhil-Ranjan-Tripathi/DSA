class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res= []

        def backtrack(curr, i):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for c in d[digits[i]]:
                curr.append(c)
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return res