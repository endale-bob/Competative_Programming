class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = defaultdict(lambda : -1)
        res = float('inf')

        for ind in range(len(cards)):
            card = cards[ind]
            if(freq[card] > -1):
                res = min(ind + 1 - freq[card], res)
            freq[card] = ind
        
        return res if res != float('inf') else -1

