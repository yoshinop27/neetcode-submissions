class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort() 
        res = [] 
        if len(nums) < 3:
            return res
        for i,num in enumerate(nums): 
            # num is the pivot
            # set up the window
            left = i + 1 # 3
            right = len(nums) - 1 # 4
            while left < right:
                total = nums[left] + nums[right] + nums[i] # 0
                # special case
                if total == 0: 
                    if (nums[i], nums[left], nums[right]) not in seen:
                        res.append([nums[i], nums[left], nums[right]])
                        seen.add((nums[i], nums[left], nums[right]))
                    left += 1
                else:
                    if total > 0:
                        right -= 1
                    else:
                        left += 1
        return res
            
            
            
