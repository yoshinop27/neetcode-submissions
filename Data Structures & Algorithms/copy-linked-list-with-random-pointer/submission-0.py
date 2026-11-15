"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        while cur:
            new = Node(cur.val)
            nxt = cur.next
            cur.next = new
            new.next = nxt
            cur = nxt
        real = head
        clone = head.next
        while clone:
            if real.random:
                cr = real.random.next
            else:
                cr = None
            clone.random = cr
            if clone.next:
                real = real.next.next
                clone = clone.next.next
            else:
                break
        real = head
        clone_head = head.next
        clone = head.next
        while clone:
            if clone.next:
                rn = real.next.next
                cn = clone.next.next
            else:
                rn, cn = None, None
            real.next = rn
            clone.next = cn
            if clone.next:
                real = rn
                clone = cn
            else:
                break
        return clone_head

        