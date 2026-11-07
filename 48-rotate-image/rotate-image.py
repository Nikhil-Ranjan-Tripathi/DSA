class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mat = matrix[::-1]
        a = [[]] * len(matrix)

        for i in range(len(mat[0])):
            curr = []
            for j in range(len(mat)):
                curr.append(mat[j][i])

            a[i] = curr
            
        for i in range(len(a)):
            matrix[i] = a[i]