class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]

        def solve(n, arr):
            if n<=1:
                return result

            a = [1]

            for i in range(len(arr)-1):
                a.append(arr[i]+arr[i+1])

            a.append(1)
            result.append(a)
            solve(n-1, a)

        solve(numRows, result[-1])

        return result
