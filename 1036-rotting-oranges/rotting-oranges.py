from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        que = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    que.append((r,c))
                if grid[r][c]==1:
                    fresh_count += 1
        if fresh_count==0:
            return 0
        
        mins = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        while que:
            if fresh_count==0:
                return mins
            mins+=1
            level_size = len(que)
            for _ in range(level_size):
                r, c = que.popleft()
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_count-=1
                        que.append((nr,nc))

        return -1 if fresh_count>0 else mins
        