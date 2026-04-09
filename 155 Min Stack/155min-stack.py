class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.length = 0

    def push(self, val: int) -> None:
        # v = val
        if self.length < len(self.stack) and self.stack[self.length] == None:
            self.stack[self.length] = val
        else:
            self.stack.append(val)

        val = min(val, self.min_stack[self.length-1] if self.length > 0 else val)

        if self.length < len(self.min_stack) and self.min_stack[self.length] == None:
            self.min_stack[self.length] = val
        else:
            self.min_stack.append(val)
    
        self.length += 1
        # print("pushed", v, "self.length:", self.length, "min_stack:", self.min_stack, "stack:", self.stack)

    def pop(self) -> None:
        if self.length > 0:
            self.stack[self.length-1] = None
            self.min_stack[self.length-1] = None
            self.length -= 1
        else:
            return None
        # print("pop", "self.length:", self.length, "min_stack:", self.min_stack, "stack:", self.stack)

    def top(self) -> int:
        return self.stack[self.length-1]

    def getMin(self) -> int:
        # print("getMin", "self.length:", self.length, "self.min_stack:", self.min_stack)
        # return self.min_stack[-1]
        if self.length > 0:
            return self.min_stack[self.length-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()