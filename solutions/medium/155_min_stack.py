class MinStack:

    def __init__(self):
        self.stack = []
        self.min_history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_history) == 0:
            self.min_history.append(val)
        elif val <= self.min_history[-1]:
            self.min_history.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.min_history) > 0 and val == self.min_history[-1]:
            self.min_history.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_history[-1] if len(self.min_history) > 0 else self.stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
