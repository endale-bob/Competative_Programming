class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        result = 0
        ind = -1
        for i in range(len(piles)//3):
            ind += 2
            result += piles[ind]
        return result
