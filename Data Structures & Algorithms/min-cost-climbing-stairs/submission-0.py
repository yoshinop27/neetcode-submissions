class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [None] * len(cost)

        def dfs(i):
            # Base case
            if i >= len(cost):
                return 0
            elif cache[i]:
                return cache[i]
            else:
                one_step = cost[i] + dfs(i+1)
                two_step = cost[i] + dfs(i+2)
                cache[i] = min(one_step, two_step)
                return cache[i]

        return min(dfs(0), dfs(1))
