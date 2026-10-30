# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val in range(p.val,q.val+1) or root.val in range(q.val,p.val+1):
            return root
        else:
            if min(p.val,q.val) > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.left, p, q)