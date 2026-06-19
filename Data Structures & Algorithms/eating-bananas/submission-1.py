class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        search = range(1, max(piles))
        left = 1
        right = len(search)  
        ret = max(piles)

        while left <= right:
            mid = (left + right) // 2
            time = 0
            for i in range(len(piles)):
                time += (piles[i] + mid - 1) // mid
            if time <= h:
                ret = min(ret, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ret

        