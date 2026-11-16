# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at each node compute how deep it is on left and right
        def depth(node):
            if not node:
                return 0, 0
            lh, ld = depth(node.left)
            rh, rd = depth(node.right)
            return max(lh, rh) + 1, max(ld, rd, lh+rh)
        return depth(root)[1]
        
        