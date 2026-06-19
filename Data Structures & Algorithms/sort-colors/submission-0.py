class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        space = [0] * 3
        for i in range(len(nums)):
            space[nums[i]] += 1
        cur = 0
        for j in range(len(space)):
            for _ in range(space[j]):
                nums[cur] = j
                cur += 1

