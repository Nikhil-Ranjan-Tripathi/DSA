class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        result = []
        
        if maze[n-1][n-1]==0 or maze[0][0]==0:
            return result
        
        def isSafe(row, col):
            return 0<=row<n and 0<=col<n and maze[row][col]==1
        
        def dfs(row, col, path):
            if row==n-1 and col==n-1:
                result.append(path)
                return
            
            directions = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]
            
            for dr, dc, direction in directions:
                new_row = row+dr
                new_col = col+dc
                
                if isSafe(new_row, new_col):
                    maze[new_row][new_col] = -1 #mark the indices
                    
                    dfs(new_row, new_col, path+direction)
                    
                    maze[new_row][new_col]=1
                    
                    
        # Mark starting cell as visited 
        maze[0][0] = -1 
        dfs(0, 0, "") 
        return result
                    
                    