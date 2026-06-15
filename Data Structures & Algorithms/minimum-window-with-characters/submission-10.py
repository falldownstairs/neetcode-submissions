class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        tmap = {}
        smap = {}
        if len(t) > len(s):
            return res

        for i in t:
            tmap[i] = tmap.get(i, 0) + 1
        matches = 0
        for i in range(len(s)):
            if s[i] in tmap.keys():
                smap[s[i]] = smap.get(s[i], 0) + 1
                if smap[s[i]] <= tmap[s[i]]:
                    matches += 1
            if matches == len(t):
                res = s[0:i+1]
                break
        ini = len(res) - 1
        l, r = 0, len(res) - 1
        while r < len(s):
            if s[r] in tmap.keys() and r != ini:
                smap[s[r]] = smap.get(s[r], 0) + 1
            while l < r:
                if s[l] in tmap.keys() and smap[s[l]] <= tmap[s[l]]:
                    break
                if s[l] in tmap.keys():
                    smap[s[l]] = smap.get(s[l], 0) - 1
                l += 1
            if r - l < len(res):
                res = s[l:r+1]
            r += 1
        return res