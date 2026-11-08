class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mv,lv,rv = nums[mid], nums[left], nums[right]

            if mv == target:
                return mid
            # right side sorted
            if rv > mv:
                if target > mv and target <= rv:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                print("hi")
                if target < mv and target >= lv:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


