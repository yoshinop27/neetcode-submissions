# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfsCheck(node, low, high):
            if not node:
                return True
            if node.val > low and node.val < high:
                left = dfsCheck(node.left, low, node.val)
                right = dfsCheck(node.right, node.val, high)
                return left and right
            else:
                return False
        
        return dfsCheck(root, -float('inf'), float('inf'))