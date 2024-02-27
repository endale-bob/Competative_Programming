class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(ind, temp, sums):
            if(ind >= len(candidates)):
                if(sums == target):
                    res.append(temp[:])
                return
            
            if(sums > target):
                return
            
            # for idx in range(ind+1, len(candidates)):
            temp.append(candidates[ind])
            backtracking(ind, temp, sums + candidates[ind])
            temp.pop()
            backtracking(ind+1, temp, sums)

            
        backtracking(0, [], 0)
        return res

            