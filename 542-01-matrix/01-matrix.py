from collections import deque

class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        if not grid:
            return []

        rows, cols = len(grid), len(grid[0])

        que = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    que.append((r, c))
                else:
                    grid[r][c] = -1
                    
        while que:

            r, c = que.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == -1):

                    grid[nr][nc] = grid[r][c] + 1
                    que.append((nr, nc))

        return grid