class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for ind in range(len(nums) -1):
            if(nums[ind] == nums[ind+1]):
                nums[ind] *= 2
                nums[ind+1] = 0
        
        left, right = 0, 0

        while(right < len(nums)):
            if(nums[right] != 0):
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1
        
        return nums