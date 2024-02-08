class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefSum1 = []
        for i in range(len(nums)):
            prefSum1.append(nums[i] + prefSum1[-1] if i > 0 else nums[i])

        prefSum2 = nums.copy()
        for i in range(len(nums) -2, -1, -1):
            prefSum2[i] = prefSum2[i+1] + prefSum2[i]

        print(prefSum1, prefSum2)
        
        for i in range(len(nums)):
            if prefSum1[i] == prefSum2[i]:
                return i
        
        return -1