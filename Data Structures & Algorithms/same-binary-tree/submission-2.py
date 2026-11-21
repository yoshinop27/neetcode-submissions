# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(pn, qn):
            # both null
            if not pn and not qn:
                return True
            # both non null
            if pn and qn:  
                if pn.val != qn.val:
                    return False
                return dfs(pn.left, qn.left) and dfs(pn.right, qn.right)
            # one null one not
            return False
             
        return dfs(p,q)