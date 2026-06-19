from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = deque()
        ret = []

        if root:
            deq.append(root)
        while len(deq) > 0:
            level = []
            for _ in range(len(deq)):
                node = deq.popleft()
                level.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            ret.append(level)
        return ret

