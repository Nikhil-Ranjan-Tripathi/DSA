class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        m = len(maze)
        
        results = []
        
        visi = [[False]*m for _ in range(m)]
        
        def is_safe(r,c):
            return (0<=r<m and 0<=c<m and maze[r][c]==1 and visi[r][c]==False)
            
        def dfs(r,c,p):
            if not is_safe(r,c):
                return
            
            if r==m-1 and c==m-1:
                results.append(p)
                
            visi[r][c]=True
            
            dfs(r+1,c,p+"D")
            dfs(r,c-1,p+"L")
            dfs(r,c+1,p+"R")
            dfs(r-1,c,p+"U")
            
            
            
            visi[r][c]=False
            
        dfs(0,0,'')
        
        return results