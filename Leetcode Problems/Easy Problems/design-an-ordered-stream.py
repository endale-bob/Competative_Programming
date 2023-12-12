class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [0]*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        result = []
        while(self.pointer < self.n and self.arr[self.pointer]):
            result.append(self.arr[self.pointer])
            self.pointer += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)