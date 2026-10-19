class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            hashmap[str(chars)].append(s)
        for key in hashmap.keys():
            sublist = []
            for value in hashmap[key]:
                sublist.append(value)
            res.append(sublist)
        return res