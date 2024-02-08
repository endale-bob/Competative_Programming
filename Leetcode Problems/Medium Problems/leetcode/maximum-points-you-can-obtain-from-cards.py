class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        right = n - k
        totalSum = sum(cardPoints)
        windowSum = sum(cardPoints[:right])

        minSum = windowSum


        for i in range(right, n):
            windowSum += cardPoints[i]
            windowSum -= cardPoints[i - right]

            minSum = min(windowSum, minSum)
        
        return totalSum - minSum
