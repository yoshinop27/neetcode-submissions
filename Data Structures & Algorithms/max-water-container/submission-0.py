class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        ret = 0
        while left < right:
            lh, rh = heights[left], heights[right]
            vol = min(lh, rh) * (right-left)
            ret = max(ret, vol)
            if lh < rh:
                left += 1
            else:
                right -= 1 
        return ret
            
