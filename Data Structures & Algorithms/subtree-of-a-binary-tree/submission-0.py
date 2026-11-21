# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(main, clone):
            # both null
            if not (main or clone):
                return True
            if main and clone:
                if main.val == clone.val:
                    return dfs(main.left, clone.left) and dfs(main.right, clone.right)
                return False
            return False

        s = []
        s.append(root)
        while s:
            cur = s.pop()
            if not cur:
                continue
            if cur.val == subRoot.val:
                if dfs(cur, subRoot):
                    return True
            s.append(cur.left)
            s.append(cur.right)
        return False