class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [None]
        for num in sorted(nums, reverse=True):
            self.heap.append(num)
        
    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i//2] < self.heap[i]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i // 2
        copy = self.heap.copy()
        ret = 0

        def popH(nums):
            root = nums[1]
            if len(nums) == 1:
                return
            if len(nums) == 2:
                return nums.pop()
            i = 1
            nums[i] = nums.pop()
            while i * 2 < len(nums):
                if i * 2 + 1 < len(nums) and nums[i*2+1] > nums[i*2] and nums[i*2+1] > nums[i]:
                    nums[i], nums[i*2+1] = nums[i*2+1], nums[i]
                    i = i*2+1
                elif nums[i*2] > nums[i]:
                    nums[i], nums[i*2] = nums[i*2], nums[i]
                    i *= 2
                else:
                    break
            return root

        for _ in range(self.k):
            ret = popH(copy)
        return ret
