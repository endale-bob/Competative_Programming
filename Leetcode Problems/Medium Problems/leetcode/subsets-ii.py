class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtracking(ind, temp):
            if(ind >= len(nums)):
                res.add(tuple(sorted(temp)))
                return
                
            temp.append(nums[ind])
            backtracking(ind+1, temp)
            temp.pop()
            backtracking(ind+1, temp)
            
        
        backtracking(0, [])
        return res