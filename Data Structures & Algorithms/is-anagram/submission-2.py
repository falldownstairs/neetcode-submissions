class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in sdict:
                sdict[i] +=1
            else:
                sdict[i] = 1
        for i in t:
            if i not in sdict or sdict[i] < 1:
                return False
            else:
                sdict[i] -= 1
        return True
