class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0]*26
        arr2 = [0]*26
        for i in range(len(s2)):
            print(arr1)
            print(arr2)
            if i < len(s1):    
                arr1[ord(s1[i])-ord('a')] += 1  
          
            arr2[ord(s2[i])-ord('a')] += 1

            if i > len(s1) - 1: 
                arr2[ord(s2[i-len(s1)])-ord('a')] -= 1

            if arr1 == arr2 and i >= len(s1) - 1:
                return True
        return False