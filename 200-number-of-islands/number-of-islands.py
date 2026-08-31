from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        que = deque()
        island = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    island += 1

                    que.append((r, c))
                    grid[r][c] = '0'

                    while que:
                        rr, cc = que.popleft()

                        for dr, dc in directions:
                            nr = rr + dr
                            nc = cc + dc

                            if (0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == '1'):

                                grid[nr][nc] = '0'
                                que.append((nr, nc))

        return island