class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        while True:
            if nums[idx] + idx >= len(nums)-1:
                return True
            elif nums[idx] == 0:
                return False
            else:
                idx = self.assessJump(nums, idx)
    
    def assessJump(self, nums, idx):
        jump = nums[idx]
        start = idx+1
        end = idx+1+jump
        cur_max = -1
        opt_idx = -1
        # select the index that will place us the farthest
        for i in range(start,min(len(nums),end)):
            if nums[i] + i >= cur_max:
                opt_idx = i
                cur_max = nums[i] + i
        return opt_idx
    