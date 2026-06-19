# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.help(preorder, inorder)

    def help(self, preorder, inorder):

        if not preorder:
            return None
        
        root = preorder[0]
        # breakdown of inorder
        left = []
        index = - 1
        for i in range(len(inorder)):
            if inorder[i] == root:
                index = i
                break
            left.append(inorder[i])
        right = inorder[index + 1:]

        # breakdown preorder
        prel = preorder[1 : len(left) + 1]
        preright = preorder[len(left) + 1 :]

        # recursive call on both sides
        rt = TreeNode(root)
        rt.left = self.help(prel, left)
        rt.right = self.help(preright, right)
        return rt