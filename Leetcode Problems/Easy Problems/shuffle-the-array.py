class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for ind in range(n):
            result.append(nums[ind])
            result.append(nums[ind + n])
        
        return result