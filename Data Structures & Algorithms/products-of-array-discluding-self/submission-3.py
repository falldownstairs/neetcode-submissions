class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        totalproduct = 1
        zeroes = 0
        for i in nums:
            if i == 0:
                zeroes += 1
            else:
                totalproduct *= i
        
        if zeroes > 1:
            return res
        elif zeroes == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = totalproduct
                    return res
        else:
            for i in range(len(nums)):
                res[i] = int(totalproduct / nums[i])

        return res

