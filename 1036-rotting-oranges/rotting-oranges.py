from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    que.append((r,c))

        if fresh==0:
            return 0
        
        mins = 0

        while que and fresh>0:

            for _ in range(len(que)):
                rr, cc = que.popleft()

                for dr, dc in directions:
                    nr = rr+dr
                    nc = cc+dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh-=1
                        que.append((nr, nc))
                
            mins+=1

        return -1 if fresh>0 else mins