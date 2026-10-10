# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        maxheap = []
        def dfs(node, maxheap):
            if len(maxheap) == k:
                if -maxheap[0] > node.val:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, -node.val)
            else:
                heapq.heappush(maxheap, -node.val)
            if(node.left):
                dfs(node.left, maxheap)
            if(node.right):
                dfs(node.right, maxheap)
        dfs(root, maxheap)
        return -maxheap[0]
        