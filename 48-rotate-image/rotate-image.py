class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l = [[0] * n for _ in range(n)]

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix)):
                l[j][n-1-i]=matrix[i][j]
        
        for i in range(n):
            matrix[i] = l[i]

