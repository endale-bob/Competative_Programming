class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # left, right = 0, len(nums) -1
        result = 0

        for left in range(len(nums)):
            right = left +1
            while(right < len(nums)):
                if(nums[left] + nums[right] < target):
                    result += 1
                right += 1
        
        return result
