class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        size = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col): 
            count = 0
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dr, dc in directions:
                r,c = row + dr, col + dc
                if ((r,c) not in seen and
                r in range(rows) and 
                c in range(cols) and 
                grid[r][c] == 1):
                    count += 1
                    seen.add((r,c))
                    count += dfs(r,c)
            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    size = max(size, dfs(row, col) + 1)
        return size