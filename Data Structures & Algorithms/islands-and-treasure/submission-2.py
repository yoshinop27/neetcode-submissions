class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c-1,1])
                    q.append([r,c+1,1])
                    q.append([r-1,c,1])
                    q.append([r+1,c,1])
        while q:
            r,c,d = q.pop(0)
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue 
            if grid[r][c] == 1 or grid[r][c] == 0:
                continue
            if grid[r][c] <= d:
                continue
            grid[r][c] = d
            for nr, nc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                q.append([nr, nc, d+1])
        
            
            
            


