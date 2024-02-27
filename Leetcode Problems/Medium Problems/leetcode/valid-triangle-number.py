class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        for idx in range(len(nums)-1, 1, -1):
            left = 0
            right = idx -1
            while(right > left):
                if(nums[right] + nums[left] > nums[idx]):
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        
        return ans
        

        