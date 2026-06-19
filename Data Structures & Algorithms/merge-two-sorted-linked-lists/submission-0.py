# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        ret = None
        while list1 or list2:
            if not list1: 
                while list2:
                    if ret:
                        ret.next = list2
                        ret = ret.next
                    else:
                        head = list2
                        ret = list2
                    list2 = list2.next
            elif not list2: 
                while list1:
                    if ret:
                        ret.next = list1
                        ret = ret.next
                    else:
                        head = list1
                        ret = list1
                    list1 = list1.next
            else:
                if list1.val <= list2.val:
                    if ret:
                        ret.next = list1
                        ret = ret.next
                    else:
                        head = list1
                        ret = list1
                    list1 = list1.next
                else:
                    if ret:
                        ret.next = list2
                        ret = ret.next
                    else:
                        head = list2
                        ret = list2
                    list2 = list2.next
        return head