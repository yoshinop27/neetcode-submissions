# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        cycle = False
        i = 0
        while fast and fast.next and slow:
            if fast == slow and i != 0:
                cycle = True
                break
            fast = fast.next.next
            slow = slow.next
            i += 1
        return cycle
