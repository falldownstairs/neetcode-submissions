class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashmap = {}
        for i in nums:
            hashmap[i] = 1
        for i in range(len(nums)):
            c = 0
            k = nums[i]
            while k in hashmap:
                c += hashmap[k]
                k += hashmap[k]
            hashmap[nums[i]] = c
            res = max(c,res)
        return res