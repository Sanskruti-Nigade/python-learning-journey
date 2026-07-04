class MinStack:
    """
    A stack data structure that retrieves the minimum element in O(1) time.
    Time Complexity for all operations (push, pop, top, getMin): O(1)
    Space Complexity: O(n) - utilizing an auxiliary tracking stack.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # The new minimum is either the value itself, or the current top of the min_stack
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        else:
            current_min = val
        self.min_stack.append(current_min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 12. Min Stack Test ---")
    
    # Initialize the min stack
    minStack = MinStack()
    
    print("Pushing elements: -2, 0, -3")
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    
    print("Current Minimum:", minStack.getMin())   # Expected Output: -3
    
    print("Popping top element...")
    minStack.pop()
    
    print("New Top Element:", minStack.top())      # Expected Output: 0
    print("New Minimum Element:", minStack.getMin())  # Expected Output: -2