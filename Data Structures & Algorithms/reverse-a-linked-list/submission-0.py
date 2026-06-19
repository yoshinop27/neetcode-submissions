# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
            
        back = None
        cur = head
        front = head.next
        while front:
            cur.next = back
            back = cur
            cur = front 
            front = front.next
        cur.next = back
        return cur
