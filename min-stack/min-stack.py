
class MinStack:
    stack = []
    size = 0
    
    min = []
    minSize = 0

    def push(self, val: int) -> None:
        if self.minSize == 0 or val <= self.min[-1]:
            self.min.append(val)
            self.minSize += 1
        
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            del self.min[-1]
            self.minSize -= 1
            
        del self.stack[-1]
        self.size -= 1

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()