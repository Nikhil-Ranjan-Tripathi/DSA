from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows, cols = len(maze), len(maze[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        sr, sc = entrance
        que = deque([(sr, sc, 0)])
        maze[sr][sc] = '+'

        while que:
            for _ in range(len(que)):
                rr, cc, dist = que.popleft()

                for dr,dc in directions:
                    nr = rr+dr
                    nc = cc+dc

                    if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]=='.':
                        if nr==0 or nc==0 or nr==rows-1 or nc==cols-1:
                            return 1+dist
                        maze[nr][nc]='+'
                        que.append((nr, nc, dist + 1))
        
        return -1

                    
