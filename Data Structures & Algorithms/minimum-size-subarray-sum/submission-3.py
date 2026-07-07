class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur = 0
        ret = float('inf')
        for r in range(0, len(nums)):
            cur += nums[r]
            # valid window
            while (cur >= target and left < len(nums)):
                ret = min(ret, r-left+1)
                cur -= nums[left]
                left += 1
        return 0 if ret == float('inf') else ret