class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        winStart, winEnd = 0, 0
        result, curr = 0, []

        while(winStart < len(nums) and winEnd < len(nums)):
            if(nums[winEnd] == 0):
                if k <= len(curr) and k != 0:
                    winStart = curr.pop(0) + 1
                elif(k == 0):
                    winStart = winEnd + 1
                curr.append(winEnd)
            
            result = max(result, winEnd - winStart + 1)
            winEnd += 1

        return result
