from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        seen = set()
        if grid[0][0] == 0:
            queue.append((0,0))
        length = 1
        directions = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        while queue:
            for i in range(len(queue)):
                row,col = queue.popleft()
                if row == rows-1 and col == cols-1:
                    return length
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(rows) and
                    c in range(cols) and 
                    grid[r][c] == 0 and 
                    (r,c) not in seen):
                        queue.append((r,c))
                        seen.add((r,c))
            length += 1
        return -1