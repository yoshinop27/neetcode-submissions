class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [[None,None] for _ in range(len(nums))]
        # forward pass
        running = 1
        for i in range(1,len(nums)):
            running *= nums[i-1]
            arr[i][0] = running
        # backward pass
        running = 1
        for j in range(len(nums)-2,-1,-1):
            running *= nums[j+1]
            arr[j][1] = running
        ret = [None] * len(nums)
        ret[0] = arr[0][1]
        ret[len(nums)-1] = arr[len(nums)-1][0]
        for k in range(1,len(nums)-1):
            ret[k] = arr[k][0]*arr[k][1]
        return ret


