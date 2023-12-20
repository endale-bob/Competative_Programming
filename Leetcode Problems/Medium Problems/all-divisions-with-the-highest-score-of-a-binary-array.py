class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        new_nums = [nums[0]]
        for i in range(1, len(nums)):
            new_nums.append(nums[i] + new_nums[-1])
        
            
        max_i = 0
        result = []

        ind = 0
        while(ind < len(nums)+1):
            nums_left = ind - new_nums[ind-1] if ind > 0 else 0
            nums_right = new_nums[-1] - new_nums[ind - 1] if ind > 0 else new_nums[-1]
            if( nums_left + nums_right > max_i ):
                result.clear()
                result.append(ind)
            elif( nums_left + nums_right  == max_i):
                result.append(ind)
            ind += 1
            max_i = max(nums_left + nums_right, max_i)
        
        return result
            
        