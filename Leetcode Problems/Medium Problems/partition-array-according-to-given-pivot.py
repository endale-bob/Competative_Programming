class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []

        for ind in range(len(nums)):
            if(nums[ind] < pivot):
                result.append(nums[ind])

        for ind in range(len(nums)):
            if(nums[ind] == pivot):
                result.append(nums[ind])

        for ind in range(len(nums)):
            if(nums[ind] > pivot):
                result.append(nums[ind])

        return result
        
