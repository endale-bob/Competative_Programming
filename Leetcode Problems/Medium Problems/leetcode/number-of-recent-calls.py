class RecentCounter:

    def __init__(self):
        self.req = deque(maxlen= 3001)

    def ping(self, t: int) -> int:
        self.req.append(t)
        while(t - 3000 > self.req[0]):
            self.req.popleft()

        return len(self.req)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)