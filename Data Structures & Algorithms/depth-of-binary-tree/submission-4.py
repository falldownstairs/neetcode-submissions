# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.search(root, 0)
    def search(self, root, depth):
        if not root: return depth
        depth += 1
        return max(self.search(root.left, depth), self.search(root.right, depth))