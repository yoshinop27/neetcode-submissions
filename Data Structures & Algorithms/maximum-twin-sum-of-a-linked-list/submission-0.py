# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        start = ListNode(None, head)
        fast = head
        slow = head
        count = 0
        while fast and fast.next:
            count += 1
            fast = fast.next.next
            slow = slow.next
        # slow now on mid right
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        res = -float("inf")
        front = head
        while count > 0:
            count -= 1
            res = max(res, prev.val + front.val)
            front = front.next
            prev = prev.next
        return res

