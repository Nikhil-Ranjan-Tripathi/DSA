from collections import deque

class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not grid:
            return grid
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        que = deque([(sr, sc)])
        c = grid[sr][sc]
        if c==color:
            return grid
            
        grid[sr][sc] = color
        while que:
            rr, cc = que.popleft()

            for dr, dc in directions:
                nr = rr+dr
                nc = cc+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==c:
                    grid[nr][nc]=color
                    que.append((nr, nc))

        return grid