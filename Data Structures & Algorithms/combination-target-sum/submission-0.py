class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = [] 
        subset = []

        def help(subset, start, total):
            if start >= len(nums):
                return
            if total == target:
                ret.append(subset.copy())
                return
            if total > target:
                return
            subset.append(nums[start])
            help(subset, start, total + nums[start])
            subset.pop()
            help(subset, start + 1, total)
            
        help(subset, 0, 0)
        return ret
