class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store = {nums[ind]: ind for ind in range(len(nums))}

        for op in operations:
            nums[store[op[0]]] = op[1]
            store[op[1]] = store[op[0]]
            del store[op[0]]

        return nums