class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = float('inf') 

    def push(self, val: int) -> None:
        self.minStack = min(self.minStack, val)
        self.stack.append([val, self.minStack])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()