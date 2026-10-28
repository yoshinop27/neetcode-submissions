class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            mid = (right + left) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
