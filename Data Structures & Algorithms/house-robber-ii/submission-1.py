class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i, start):
            if(i >= len(nums) or (i >= len(nums)-1 and start and len(nums) != 1)):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1, start), nums[i] + dfs(i+2, start))
            return memo[i]
        a = dfs(1,False)
        memo = [-1] * len(nums)
        b = dfs(0,True)
        return max(a,b)


            