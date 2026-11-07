class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h = []
        v = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    h.append(i)
                    v.append(j)

        def hori(i):
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        def vert(j):
            for i in range(len(matrix)):
                matrix[i][j] = 0

        for i in h:
            hori(i)

        for i in v:
            vert(i)
        