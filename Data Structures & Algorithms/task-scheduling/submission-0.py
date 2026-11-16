import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        num_max = len([1 for freq, val in counts.items() if val == max_freq])
        return max((max_freq - 1)*(n+1)+num_max, len(tasks))