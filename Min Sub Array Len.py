class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        result, minLen = 0, float("inf")

        while(left < len(nums) and right < len(nums)):
            result += nums[right]

            if(result < target):
                right += 1
            elif(result == target):
                    minLen = min(minLen, right - left + 1)
                    right += 1
            else:
                result -= nums[right]
                result -= nums[left]
                left += 1
            

        return minLen if minLen != float("inf") else 0
