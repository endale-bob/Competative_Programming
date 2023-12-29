class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for num in nums:
            if(num == 0): red += 1
            elif(num == 1): white += 1
            else: blue += 1

        for ind in range(len(nums)):
            if(red > 0):
                red -= 1
                nums[ind] = 0
            elif(white > 0):
                white -= 1
                nums[ind] = 1
            else:
                nums[ind] = 2
        
        return nums
        
        