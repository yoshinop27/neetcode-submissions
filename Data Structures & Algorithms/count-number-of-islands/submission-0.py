class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Set up vars
        rows, cols = len(grid), len(grid[0])
        count = 0
        seen = set()

        def dfs(row, col):
            positions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dr, dc in positions:
                r,c = row + dr, col + dc
                if not ((r,c) in seen or 
                r not in range(rows) or 
                c not in range(cols) or 
                grid[r][c] == '0'):
                    seen.add((r,c))
                    dfs(r,c) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    count += 1
                    seen.add((r,c))
                    dfs(r,c)
        return count