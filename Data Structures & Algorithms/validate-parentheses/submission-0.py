class Solution:
    def isValid(self, s: str) -> bool:
            # Dictionary to hold the matching pairs
        matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of open brackets
        stack = []
    
    # Iterate through each character in the string
        for char in s:
            if char in matching_bracket:
            # If stack is not empty, get the top element, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
            # Check if the top element matches the corresponding opening bracket
                if matching_bracket[char] != top_element:
                    return False
            else:
            # If it's an open bracket, push onto the stack
                stack.append(char)
    
    # If stack is empty, all brackets matched correctly
        return not stack
        