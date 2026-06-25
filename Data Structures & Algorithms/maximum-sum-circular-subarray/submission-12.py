class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        window = 0
        cursum = 0
        minsum = 0
        minwin = 0
        for i in range(len(nums)*2-1):
            # reset cases
            if window == len(nums) or cursum >= 0:
                cursum = 0
                window = 0
            cursum += nums[i% len(nums)]
            window += 1
            if cursum < minsum:
                minsum = cursum
                minwin = window
                print(f"window: {window}" )
                print(f"minsum {minsum}")
                print(i % len(nums))
        if minwin == len(nums):
            return max(nums)
        else:
            return max(max(nums), total - minsum)

            
            
            