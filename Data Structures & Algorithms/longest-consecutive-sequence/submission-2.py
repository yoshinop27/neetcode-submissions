class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        res = 1
        for num in numset:
            if num-1 in numset:
                continue
            stride = 1
            while num+stride in numset:
                res = max(res, stride+1)
                stride += 1
        return res
            
        