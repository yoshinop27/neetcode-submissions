class Solution:

    def rob_help(self, nums):
        dp = [0] * len(nums)
        start = max(nums[0], nums[1])
        dp[0], dp[1] = nums[0], start
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return max(dp)

    def rob(self, nums: List[int]) -> int:
        # trivial example
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        # seperate the circular cases
        first = nums[:-1]
        second = nums[1:]
        first_res = self.rob_help(first)
        sec_res = self.rob_help(second)
        return max(first_res, sec_res)

    

            


