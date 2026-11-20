# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if a binary tree is balanced -> left and right height differ by 1
            # if we have the height of left/right subtree we obtained the answer for a single node
        def dfs(root) -> int:
            # if just a leaf return 1
            if not root:
                return 1
            # find height of left
            left = dfs(root.left)
            # find height of right
            right = dfs(root.right)
            # if not balanced return -1
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            # return height of this subtree
            return max(left,right) + 1
        
        if dfs(root) == -1:
            return False
        return True