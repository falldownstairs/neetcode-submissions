class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        arr1 = [0]*26
        arr2 = [0]*26

        for i in range(len(s1)):
            arr1[ord(s1[i])-ord('a')] += 1 
            arr2[ord(s2[i])-ord('a')] += 1
        for i in range(26):
            if arr1[i] == arr2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            p = ord(s2[l]) - ord('a')


            arr2[p] -= 1
            if arr2[p] == arr1[p]:
                matches += 1
            elif arr2[p] + 1 == arr1[p]:
                matches -= 1
            
            p = ord(s2[r]) - ord('a')

            arr2[p] += 1
            if arr2[p] == arr1[p]:
                matches += 1
            elif arr2[p] - 1 == arr1[p]:
                matches -= 1
            
            l += 1
        return matches == 26