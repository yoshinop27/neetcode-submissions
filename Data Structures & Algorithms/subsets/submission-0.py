class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def help(i, subset):
            if i >= len(nums):
                ret.append(subset.copy())
                return 

            # pop off num 
            num = nums[i]
            # yes case
            subset.append(num)
            help(i+1, subset)
            # no case
            subset.pop()
            help(i+1, subset)

        help(0, [])
        return ret
