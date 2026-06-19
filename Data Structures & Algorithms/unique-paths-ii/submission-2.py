class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = []
        for i in range(m):
            cache.append([None] * n)


        def dfs(row,col, cache):
            # Base Cases
            if row >= m or col >= n:
                return 0
            if obstacleGrid[row][col]:
                return 0
            if row == m-1 and col == n-1:
                return 1
            
            # Check Cache
            if cache[row][col] != None:
                return cache[row][col]

            # Add to cache
            cache[row][col] = dfs(row+1, col, cache) + dfs(row, col+1, cache)
            # Recurse
            return cache[row][col]
        
        return dfs(0,0, cache)
