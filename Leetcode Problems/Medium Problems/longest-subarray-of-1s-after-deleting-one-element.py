class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        winStart, winEnd = 0, 0
        store, result = -1, 0
        minus = 0

        while(winStart < len(nums) > winEnd):
            if(nums[winEnd] == 0):
                if(store >= winStart):
                    winStart = store + 1
                store = winEnd
                minus = 1
            else:
                result = max(result, winEnd - winStart+1-minus)
            winEnd += 1
        if result == len(nums): result -=1
        return result
                