# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root: queue = [root]
        else: return res
        while len(queue) > 0:
            res.append([])
            for _ in range(len(queue)):
                n = queue.pop(0)
                res[-1].append(n.val)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
        return res
