class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for m in range(len(s)):
            l, r = m, m
            while((l >= 0 and r < len(s)) and s[r] == s[l]):
                l -= 1
                r += 1
                res += 1
            l, r = m, m + 1
            while((l >= 0 and r < len(s)) and s[r] == s[l]):
                l -= 1
                r += 1
                res += 1
        return res