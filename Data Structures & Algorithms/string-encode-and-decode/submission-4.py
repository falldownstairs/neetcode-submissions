class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ";" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = 0
        temp = ""
        while i < len(s):
            if n == 0:
                if s[i] == ';':
                    n = int(temp)
                    if n == 0:
                        res.append("")
                    temp = ""
                else:
                    temp += s[i]
            else:
                temp += s[i]
                if n == 1:
                    res.append(temp)
                    temp = ""
                n -= 1
            i += 1
        return res
