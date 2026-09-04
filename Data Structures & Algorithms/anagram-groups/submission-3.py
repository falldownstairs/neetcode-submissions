class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsMap = {}
        for string in strs:
            chars = [0] * 26
            for c in string:
                chars[ord(c) - ord('a')] += 1
            if tuple(chars) in charsMap:
                charsMap[tuple(chars)].append(string)
            else:
                charsMap[tuple(chars)] = [string]
        return list(charsMap.values())
    
    # ["act", "cat", "bat"]
    #