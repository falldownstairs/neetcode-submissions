class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        print(nums)
        for s in range(len(nums)-1,1,-1):
            if s < len(nums)-1 and nums[s] == nums[s+1]:
                continue
            l = 0
            r = s - 1
            while r>l:
                if nums[l]+nums[r]+nums[s] > 0:
                    r -= 1
                elif nums[l]+nums[r]+nums[s] < 0:
                    l += 1
                else:
                    res.append([nums[l],nums[r],nums[s]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

        