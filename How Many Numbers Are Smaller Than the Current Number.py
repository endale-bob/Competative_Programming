class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newNum = {}
        sortedNum = sorted(nums)
        result = []
        for ind in range(len(nums)):
            if(not sortedNum[ind] in newNum):
                newNum[sortedNum[ind]] = ind
            
        for num in nums:
            result.append(newNum[num])

        return result
