class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.target = target
        self.length = len(nums)
        def search(arr, s, index):
            if s == self.target:
                self.res.append(arr)
                return
            elif s > self.target:
                return
            for i in range(index, self.length):
                arr.append(nums[i])
                search(arr.copy(), s + nums[i], i)
                arr.pop()
        search([], 0, 0)
        return self.res
