class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking( lst=[], mask = 0):

            if(len(lst) == len(nums)):
                res.append(lst)
                return 

            for idx, num in enumerate(nums):
                if(mask & (1 << idx)): 
                    continue

                backtracking(lst + [num], mask | (1 << idx) )

        
        backtracking()
        return res