class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        for string in strs:
            key = [0]*26
            for c in string:
                key[ord(c) - ord('a')] += 1
            key=tuple(key)
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        return list(hashmap.values())