class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        monoS = []
        res = [-1]*len(nums)

        for ind in range(2*len(nums)):
            ind = ind%len(nums)
            while(monoS and nums[ind] > nums[monoS[-1]]):
                temp = monoS.pop()
                res[temp] = nums[ind]
            monoS.append(ind)
        
        return res

