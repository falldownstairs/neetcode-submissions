class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        def search(subset, n):
            if n == len(self.nums) + 1:
                return
            else:
                self.res.append(subset)
            for i in range(n, len(self.nums)):
                subset.append(self.nums[i])
                search(subset.copy(), i + 1)
                subset.pop()
        search([], 0)
        return self.res