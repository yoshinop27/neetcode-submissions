# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # easy case
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left 
            else:
                root.val = self.findMin(root.right)
                root.right = self.deleteNode(root.right, root.val) 
        return root           

    def findMin(self, root) -> int:
        while root and root.left:
            root = root.left
        return root.val