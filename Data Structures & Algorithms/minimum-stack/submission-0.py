class MinStack:

    def __init__(self):
        """
        Initialize the stack object.
        """
        self.stack = []
        self.min_stack = []       

    def push(self, val: int) -> None:
        """
        Push the element val onto the stack.
        """
        self.stack.append(val)
        # If min_stack is empty or val is less than or equal to the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if self.stack:
            # Pop the element from the stack
            val = self.stack.pop()
            # If the popped element is the current minimum, pop it from the min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        """
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None
