class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        store = defaultdict(lambda : -1)

        while(l < len(nums) and r < len(nums)):
            if(store[nums[l]] == -1):
                store[nums[l]] = l
                l += 1
            else:
                r = l
                while(r < len(nums) and store[nums[r]] != -1):
                    r += 1
                if(r >= len(nums)): break
                nums[l] = nums[r]
                store[nums[l]] = l
                l += 1
        
        return l 
