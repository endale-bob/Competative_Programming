class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        store = deque(tickets)
        res = 0
        while(store):
            temp = store.popleft()
            if(temp != 0):
                res += 1
                temp -= 1
            k -= 1
            if(k == -1): k = len(tickets)-1
            store.append(temp)
            if(store[k] == 0):
                return res
            
