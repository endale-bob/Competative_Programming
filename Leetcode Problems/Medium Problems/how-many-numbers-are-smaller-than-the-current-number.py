class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = sorted(nums)
        store = {}

        for i in range(len(new_nums)):
            if(new_nums[i] not in store):
                store[new_nums[i]] = i

        output = []
        for num in nums:
            ind = store[num]
            output.append(ind)
        
        return output
