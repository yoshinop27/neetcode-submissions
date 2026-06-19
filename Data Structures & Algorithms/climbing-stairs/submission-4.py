class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.climbStairsH(n, cache);
        
    def climbStairsH(self, n, cache):
        if n < 4:
            return n
        if n in cache.keys():
            return cache[n]

        cache[n] = self.climbStairsH(n-1, cache) + self.climbStairsH(n-2, cache) 
        return cache[n]
# each step choose +1 +2