class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        left, right = 0, 0

        while(right < len(nums)):
            temp = 0
            while(right < len(nums) and nums[right]== nums[left]):
                temp +=1
                right +=1
            left = right
            result += (temp)*(temp+1)//2
            temp = 0
        
        return result - len(nums)


        