class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        pointer = 0
        result = 0

        while(pointer + 2 < len(nums)):
            if(nums[pointer] + nums[pointer+1] > nums[pointer+2]):
                result = max(result, nums[pointer] + nums[pointer+1] + nums[pointer+2])
            pointer += 1
        
        return result