class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        flipTimes = 0
        max_ind = float("-inf")
        result = 0

        for flip in flips:
            flipTimes += 1
            max_ind = max(flip, max_ind)
            if(flipTimes == max_ind):
                result += 1
        
        return result

