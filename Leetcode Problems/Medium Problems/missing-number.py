class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = (len(nums)) * (len(nums)+1) / 2
        current_sum = sum(nums)

        return int(expected_sum - current_sum )
