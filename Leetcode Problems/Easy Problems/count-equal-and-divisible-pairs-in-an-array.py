class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0

        while(len(nums) > 0):
            for j in range( len(nums)-1):
                if(nums[-1] == nums[j] and ((len(nums)-1)*j)%k == 0):
                    result += 1
            nums.pop()

        
        return result
                    