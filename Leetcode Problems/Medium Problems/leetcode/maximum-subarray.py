class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        window_sum, max_sum = 0, float(-inf)

        while(right< len(nums)):
            window_sum += nums[right]
            right += 1

            max_sum = max(window_sum, max_sum)

            while(window_sum < 0):
                window_sum -= nums[left]
                left += 1
         
        return max_sum




        

