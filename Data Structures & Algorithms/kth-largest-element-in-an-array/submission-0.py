from collections import defaultdict
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = []
        for num in nums:
            neg.append(-num)
        heapq.heapify(neg)
        i = 0
        last = -1
        while i < k:
            last = -1 * heapq.heappop(neg)
            i += 1
        return last
        