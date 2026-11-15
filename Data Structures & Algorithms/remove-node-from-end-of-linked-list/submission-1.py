# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        # edge case
        if length < 2:
            return None
        # walk to length-n+1 node
        cur = head
        prev = None
        for _ in range(length-n):
            prev = cur
            cur = cur.next
        if not prev:
            return head.next
        prev.next = cur.next
        return head
        