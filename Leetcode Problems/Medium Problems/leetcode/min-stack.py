class MinStack:

    def __init__(self):
        self.store = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.store.append(val)
        if(len(self.minstack) == 0 or self.minstack[-1] >= val):
            self.minstack.append(val)

    def pop(self) -> None:
        if(len(self.store) > 0):
            ele = self.store.pop()
            if(len(self.minstack) > 0 and self.minstack[-1] == ele):
                self.minstack.pop()

    def top(self) -> int:
        return self.store[-1] if len(self.store) > 0 else None

    def getMin(self) -> int:
        return self.minstack[-1] if len(self.minstack) > 0 else None

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()