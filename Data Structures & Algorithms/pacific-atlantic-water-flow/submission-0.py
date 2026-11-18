class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 

        def dfs(r,c):
            s = [[r,c]]
            pacific = False
            atlantic = False
            seen = set()
            seen.add((r,c))
            while s:
                nr, nc = s.pop()
                if nr == 0 or nc == 0:
                    pacific = True
                if nc == len(heights[0]) - 1 or nr == len(heights) - 1:
                    atlantic = True
                height = heights[nr][nc]
                for row, col in [[nr+1,nc], [nr-1,nc], [nr,nc+1],[nr,nc-1]]:
                    if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
                        continue
                    if height >= heights[row][col]:
                        if (row,col) not in seen:
                            s.append((row,col))
                        seen.add((row,col))
            return pacific and atlantic

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i,j):
                    res.append([i,j])
        return res
