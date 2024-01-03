class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        store = {}

        while(left < len(nums)):
            if(nums[left] in store):
                while(right < len(nums) and nums[right] in store):
                    right += 1
                if(right < len(nums)):
                    nums[right], nums[left] = nums[left], nums[right]
                else:
                    return left
            store[nums[left]] = 1
            left += 1

        