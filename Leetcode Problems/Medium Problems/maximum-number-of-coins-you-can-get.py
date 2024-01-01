class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0

        for pile in piles:
            piles.pop()
            result += piles.pop()

        return result