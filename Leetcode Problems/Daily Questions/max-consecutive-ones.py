class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCons = 0
        temp = 0

        for num in nums:
            if(num == 0):
                maxCons = max(temp, maxCons)
                temp = 0
                continue
            temp += 1

        maxCons = max(temp, maxCons)
        
        return maxCons