class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        a = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    a.append([i,j])
                
        for i in range(len(a)):
            b=a[i][0]
            c=a[i][1]
            mat[b] = [0]*m
            for i in range(len(mat)):
                mat[i][c] = 0
                
        return mat