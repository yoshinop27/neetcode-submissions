# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        count = [0]
        return self.ioh(root, count, k)

    def ioh(self, root, count, k):
        if not root:
            return

        left = self.ioh(root.left, count, k)
        if left:
            return left
        count[0] += 1
        if count[0] == k:
            return root.val
        right = self.ioh(root.right, count, k)
        if right:
            return right
