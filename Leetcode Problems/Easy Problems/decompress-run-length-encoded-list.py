class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        left, right = 0,1
        result = []

        while(right < len(nums)):
            result.extend([nums[right]]*nums[left])
            right += 2
            left += 2
        
        return result