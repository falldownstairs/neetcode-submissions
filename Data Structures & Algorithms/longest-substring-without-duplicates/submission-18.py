class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seenchars = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seenchars:
                seenchars.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            seenchars.add(s[r])
        return res