class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = Best)
        return " ".join([i[:-1] for i in s])

class Best:
    def __init__(self, s):
        self.s = s[:len(s)-1]
        self.ind = s[-1]
    def __lt__(self, other):
        return self.ind < other.ind