class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            nxt = nums[fast]
            nni = nums[nxt]
            s_nxt = nums[slow]
            fast = nni
            slow = s_nxt
            if fast == slow:
                break
        slow = 0
        while slow != fast:
            fnxt = nums[fast]
            snxt = nums[slow]
            fast = fnxt
            slow = snxt
        return slow