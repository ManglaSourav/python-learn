

class MinStack:

    def __init__(self):
        self.stack = []  # pair of current value and min value

    def push(self, val: int) -> None:
        # self.stack
        if self.stack:
            min_value = min(self.stack[-1][1], val)
            self.stack.append([val, min_value])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack and self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack and self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(8)
# obj.pop()
param_3 = obj.top()
print(obj.top())
param_4 = obj.getMin()
print(param_4)
