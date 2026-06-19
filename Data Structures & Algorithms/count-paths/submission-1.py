class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        if m < 2:
            return m
        for i in range(m-2, -1, -1):
            cur = [0] * n
            cur[-1] = 1
            for j in range(n-2, -1, -1):
                cur[j] = prev[j] + cur[j+1]
            prev = cur
        return cur[0]