class Solution:
    def isValid(self, s: str) -> bool:
        openbrackets = ['(','[','{']
        closebrackets = [')',']','}']
        stack = []
        for char in s:
            if char in openbrackets:
                stack.append(char)
            elif len(stack) > 0:
                o = stack.pop()
                for i in range(3):
                    if o == openbrackets[i] and char != closebrackets[i]:
                        return False
            else:
                return False
        return len(stack) == 0