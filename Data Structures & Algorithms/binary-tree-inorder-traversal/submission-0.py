# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        ret = []
        return self.ioh(root, ret)
    
    def ioh(self, root, ret):
        if not root:
            return
        self.ioh(root.left, ret)
        ret.append(root.val)
        self.ioh(root.right, ret)
        return ret