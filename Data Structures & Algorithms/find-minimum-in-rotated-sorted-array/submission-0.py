class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            if right - left == 1:
                return min(nums[right], nums[left])
            mid = (right + left) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid
        return nums[left]
