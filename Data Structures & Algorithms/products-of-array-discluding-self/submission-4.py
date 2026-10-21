class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        preproduct, postproduct = 1,1
        for i in range(len(nums) - 1):
            preproduct *= nums[i]
            pre[i+1] = preproduct
        for i in range(-1, -len(nums), -1):
            postproduct *= nums[i]
            post[i-1] = postproduct
        for i in range(len(res)):
            res[i] = pre[i] * post[i]

        return res

