class Solution:
    def spirallyTraverse(self, mat):

        arr = []

        l = 0
        r = len(mat[0]) - 1
        u = 0
        d = len(mat) - 1

        while l <= r and u <= d:

            for i in range(l, r + 1):
                arr.append(mat[u][i])

            u += 1

            for i in range(u, d + 1):
                arr.append(mat[i][r])

            r -= 1

            if u <= d:
                for i in range(r, l - 1, -1):
                    arr.append(mat[d][i])

                d -= 1

            if l <= r:
                for i in range(d, u - 1, -1):
                    arr.append(mat[i][l])

                l += 1

        return arr