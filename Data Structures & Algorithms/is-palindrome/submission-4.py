class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)-1,-1,-1):
            if (ord(s[i]) < ord('a') or ord(s[i]) > ord('z')) and (ord(s[i]) < ord('A') or ord(s[i]) > ord('Z')) and (ord(s[i]) < ord('0') or ord(s[i]) > ord('1')):
                s = s[:i] +s[i+1:]
        s = s.lower()
        print(s)

        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True