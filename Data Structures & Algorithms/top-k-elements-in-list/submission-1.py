from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        for num in nums:
            table[num]+=1
        arr = [[] for _ in range(len(nums)+1)] 
        for ke,v in table.items():
            arr[v].append(ke)
        ret = []
        for i in range(len(nums),-1,-1):
            if arr[i]:
                ret += arr[i]
        print(ret)
        return ret[:k]


