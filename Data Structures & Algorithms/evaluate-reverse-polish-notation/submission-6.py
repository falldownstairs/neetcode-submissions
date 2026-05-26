class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2 / v1))
            else:
                stack.append(int(i))
        return stack[-1]