class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path, res = [], []
        
        def dfs(idx):
            if idx >= len(nums):
                res.append(path[:])
                return
            path.append(nums[idx])
            dfs(idx+1)
            path.pop()
            j = idx + 1
            while j<len(nums) and nums[idx] == nums[j]:
                j+=1
            dfs(j)
        
        dfs(0)
        return res
