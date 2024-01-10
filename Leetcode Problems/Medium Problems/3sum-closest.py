class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        final = float('inf')
        for i in range(len(nums)):
            p1 = i+1
            p2 = len(nums)-1
            current = float('inf')
            while(p1 < p2 ):
                if(abs(current - target) >= abs(nums[i]+nums[p1] + nums[p2] - target)):
                    current = nums[i] + nums[p1] + nums[p2] 
                if(nums[i] + nums[p1] + nums[p2] == target):
                    return target
                elif(nums[i] + nums[p1] + nums[p2] > target):
                    p2 -= 1
                else:
                    p1 += 1
            
            if(abs(current - target) <= abs(final - target)):
                    final = current 
        return final

        

        