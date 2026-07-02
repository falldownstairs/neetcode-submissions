# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def dfs(r):
            if self.res or not r:
                return
            elif self.isSameTree(r, subRoot):
                self.res = True
            else:
                dfs(r.left)
                dfs(r.right)
        dfs(root)
        return self.res
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(r1, r2):
            if not r1 and not r2:
                return
            elif (r1 and not r2) or (r2 and not r1):
                self.res = False
                return
            elif r1.val != r2.val:
                self.res = False
                return
            dfs(r1.left, r2.left)
            dfs(r1.right, r2.right)
        dfs(p,q)
        return self.res