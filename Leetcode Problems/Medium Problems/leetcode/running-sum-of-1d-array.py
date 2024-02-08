class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        curr = 0
        for num in nums:
            res.append(curr + num)
            curr = res[-1]
        
        return res