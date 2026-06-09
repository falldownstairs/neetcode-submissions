class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seenchars = set()
        l = 0
        for r in range(0, len(s)):
            if s[r] in seenchars:
                while True:
                    if s[l] == s[r]:
                        l += 1
                        break
                    else:
                        seenchars.remove(s[l])
                    l += 1
            res = max(res, r-l+1)
            seenchars.add(s[r])
        return res