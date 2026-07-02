# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(node, h):
            if not node: return
            if len(self.res) <= h:
                self.res.append(node.val)
            else:
                self.res[h] = node.val
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        dfs(root, 0)
        return self.res