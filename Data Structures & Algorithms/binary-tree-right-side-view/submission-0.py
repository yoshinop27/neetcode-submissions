from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deq = deque()
        ret = []
        
        if root:
            deq.append(root)
        
        while len(deq) > 0:
            iter = len(deq)
            for i in range(iter):

                # retrieve note
                node = deq.popleft()

                if i == iter - 1:
                    ret.append(node.val)

                # add children
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return ret