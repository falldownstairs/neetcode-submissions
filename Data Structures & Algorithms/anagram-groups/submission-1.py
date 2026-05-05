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
                output[hashmap[key]].append(string)
            else:
                output.append([string])
                hashmap[key] = len(output)-1
        return output