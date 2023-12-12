class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {nums[ind]: ind for ind in range(len(nums))}

        for ind in range(len(nums)):
            diff = target - nums[ind]
            if ( diff in store and store[diff] != ind ) :
                return [ind, store[diff]]
