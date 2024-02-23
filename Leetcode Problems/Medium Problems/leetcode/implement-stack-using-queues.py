class Queue:
    def __init__(self):
        self.q = []
        self.start = 0
        self.end = len(self.q)

    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        return self.q.pop(0)
    def front(self):
        return self.q[0]
    def rear(self):
        return self.q[-1]

    def __len__(self):
        return len(self.q)
    def __iter__(self):
        return self
    def __next__(self):
        if(self.start >= self.end):
            raise StopIteration
        else:
            self.start += 1
            return self.start -1
    def __str__(self):
        return str(self.q)

class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.enqueue(x)

    def pop(self) -> int:
        # if(len(self.q) == 1): 
        #     print(self.q)
        #     return self.q.dequeue()
        self.temp = Queue()
        val = self.q.rear()

        for i in range(len(self.q)-1):
            self.temp.enqueue(self.q.dequeue())
        
        self.q = self.temp

        return val
        

    def top(self) -> int:
        return self.q.rear()

    def empty(self) -> bool:
        print(self.q)
        if(len(self.q) == 0):
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()