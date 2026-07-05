# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.root = root
        def dfs(root, MIN, MAX):
            if not root: return
            if root.left and (root.left.val <= MIN or root.left.val >= root.val):
                self.res = False
            if root.right and (root.right.val >= MAX or root.right.val <= root.val):
                self.res = False
            dfs(root.left, MIN, root.val)
            dfs(root.right, root.val, MAX)
        dfs(root, -float("infinity"), float("infinity"))
        return self.res
    
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     self.res = True
    #     c = 0
    #     q = deque()
    #     q.append(root)

    #     while len(q) > 0:
    #         if len(q) != 2 ** c:
    #             return False
    #         for _ in range(len(q)):
    #             print(root.val)
    #             root = q.popleft()
    #             if (root.left and not root.right) or (root.right and not root.left):
    #                 return False
    #             elif root.left and root.left.val >= root.val:
    #                 return False
    #             elif root.right and root.right.val <= root.val:
    #                 return False
    #             if root.right:
    #                 q.append(root.right)
    #             if root.left:
    #                 q.append(root.left)
    #         c += 1
    #     return True