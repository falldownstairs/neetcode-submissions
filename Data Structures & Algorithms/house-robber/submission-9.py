class Solution:
    def rob(self, nums: List[int]) -> int:
        self.housemap = {}
        def dfs(n):
            if n >= len(nums):
                return 0
            if n in self.housemap.keys():
                return self.housemap[n]
            else:
                count = nums[n] + max(dfs(n+2), dfs(n+3))
                self.housemap[n] = count
                return count
        return max(dfs(0), dfs(1))
        