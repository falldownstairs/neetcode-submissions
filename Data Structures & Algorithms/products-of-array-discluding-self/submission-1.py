class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res[i] *= nums[j]
            for j in range(0, i):
                res[i] *= nums[j]
        return res