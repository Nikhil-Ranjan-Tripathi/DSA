class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        # code here
        m = len(maze)
        
        paths = []
        
        visited = [[False]*m for _ in range(m)]
        
        def is_safe(r,c):
            return (0<=r<m and 0<=c<m and maze[r][c]==1 and visited[r][c]==False)
                
        
        def dfs(r,c,path):
            if not is_safe(r,c):
                return
            
            if r==m-1 and c==m-1:
                paths.append(path)
                return
            
            visited[r][c]=True
            
            dfs(r+1,c,path+'D')
            dfs(r, c-1, path +'L')
            dfs(r,c+1,path+'R')
            dfs(r-1,c,path+'U')
            
            visited[r][c]=False
            
        dfs(0,0,'')
        
        return paths