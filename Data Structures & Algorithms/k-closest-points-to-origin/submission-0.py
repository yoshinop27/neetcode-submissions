import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dsts = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            dsts.append([dist,x,y])
        heapq.heapify(dsts)
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(dsts)[1:])

        return ret