class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path, res = [], []
        
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
            # try each number except the ones that are already in path
            for num in nums:
                # no repeats
                if num in path:
                    continue
                path.append(num)
                dfs()
                path.pop()
        
        dfs()
        return res
