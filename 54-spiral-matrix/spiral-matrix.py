class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        l = 0
        r = len(mat[0])-1
        t = 0
        b = len(mat)-1
        a = []
        while l<=r and t<=b:
            for i in range(l, r+1):
                a.append(mat[t][i])
            t+=1
            for i in range(t, b+1):
                a.append(mat[i][r])
            r-=1
            if t<=b:
                for i in range(r, l-1, -1):
                    a.append(mat[b][i])
                b-=1
            if l<=r:
                for i in range(b, t-1, -1):
                    a.append(mat[i][l])
                l+=1

        return a