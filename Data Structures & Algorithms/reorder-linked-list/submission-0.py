# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next 
        slow.next = None
        back = None
        while second:
            nxt = second.next
            second.next = back
            back = second
            second = nxt
        # merge
        front = head
        while back:
            temp_fr = front.next
            temp_b = back.next
            front.next = back
            back.next = temp_fr
            back = temp_b
            front = temp_fr

            