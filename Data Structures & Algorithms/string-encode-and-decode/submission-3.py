class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            o = ''
            for _ in range(int(length)):
                o += s[i]
                i += 1
            res.append(o)
        return res