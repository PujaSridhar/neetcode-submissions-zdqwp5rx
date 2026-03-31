class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in match:
                topElement = stack.pop() if stack else "#"
                print(topElement,i)
                if match[i] != topElement:
                    return False
            else:
                stack.append(i)
        return not stack
                    