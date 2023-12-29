class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        op, result = 0, 0

        for ind in range(1, len(nums)):
            if(nums[ind] != nums[ind-1]):
                op += 1
            result += op
        
        return result
            
