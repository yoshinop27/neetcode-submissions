# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumH(root, targetSum, 0)
    
    def hasPathSumH(self, cur, target, count):
        # if nothing return
        if not cur:
            return False

        count += cur.val

        # if leaf check
        if not cur.left and not cur.right:
            if count == target:
                return True
            return False
        
        # go left and right
        if self.hasPathSumH(cur.left, target, count):
            return True
        if self.hasPathSumH(cur.right, target, count):
            return True
        
        return False