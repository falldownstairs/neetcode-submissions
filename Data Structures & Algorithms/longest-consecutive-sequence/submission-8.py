class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for i in num_set:
            if i-1 not in num_set:
                c = 0
                num = i
                while num in num_set:
                    num+=1
                    c+=1
                res = max(res,c)
        return res

