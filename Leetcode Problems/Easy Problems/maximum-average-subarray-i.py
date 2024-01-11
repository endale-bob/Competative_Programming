class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ave, temp = sum(nums[:k]), sum(nums[:k])
        
        for winEnd in range(k, len(nums)):
            temp += nums[winEnd] - nums[winEnd - k]
            ave = max(temp, ave)

        return ave/k

        