# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root, h):
            if not root: return h
            
            l = dfs(root.left, h + 1)
            r = dfs(root.right, h + 1)


            if abs(l - r) > 1:
                self.res = False
            return max(l, r)

        dfs(root, 0)
        return self.res
        