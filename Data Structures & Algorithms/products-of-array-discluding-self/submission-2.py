class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        l = [1]*size
        r = [1]*size
        res = [1]*size

        prev = 1
        for i in range(size-2,-1,-1):
            l[i] = prev * nums[i+1]
            prev = l[i]
        print(l)
        prev = 1
        for i in range(1,size):
            r[i] = prev * nums[i-1]
            prev = r[i]
        print(r)
        for i in range(size):
            res[i] = r[i]*l[i]


        return res