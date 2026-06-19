from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        seen = set()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        seconds = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        if not fresh:
            return 0

        while queue:
            if fresh == 0:
                return seconds
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(rows) and
                    c in range(cols) and 
                    grid[r][c] == 1 and
                    (r,c) not in seen):
                        queue.append((r,c))
                        seen.add((r,c))
                        fresh -= 1
            seconds += 1
        return -1