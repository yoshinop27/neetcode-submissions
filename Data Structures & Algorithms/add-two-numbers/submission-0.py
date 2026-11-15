# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one, two = l1, l2
        # move to last pointers
        carry = 0
        prev = None
        first = True
        while one or two or carry:
            if one:
                ov = one.val
            else:
                ov = 0
            if two:
                tv = two.val
            else:
                tv = 0
            total = ov + tv + carry
            carry = total // 10
            new = ListNode(total % 10)
            # keep reference to head
            if first:
                res = new
                first = False
            # setup the next
            if prev:
                prev.next = new
            prev = new
            # move forward in list
            if one:
                one = one.next
            if two:
                two = two.next
        return res
        