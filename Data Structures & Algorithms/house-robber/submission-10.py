class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(n):
            if n >= len(nums):
                return 0
            if memo[n] != -1:
                return memo[n]
            else:
                memo[n] = max(dfs(n+1), nums[n] + dfs(n+2))
                return memo[n]
        return dfs(0)
        