class Solution:
    def rob(self, nums: List[int]) -> int:
        cur = [0, nums[0]]

        i = 1
        while i <= len(nums) - 1:
            temp = cur[1]
            cur[1] = max(cur[1], cur[0] + nums[i])
            cur[0] = temp
            i+=1
        return cur[1]
        
    # rob -> not rob
    # not rob -> rob, not rob


    # current max of n
        # current max of n - 1 || current max of n - 2 + nums[n]
