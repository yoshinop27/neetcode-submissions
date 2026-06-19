class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        cursum = 0
        for num in nums:
            cursum = max(0, cursum)
            cursum += num
            maxsum = max(maxsum, cursum)
        return maxsum
