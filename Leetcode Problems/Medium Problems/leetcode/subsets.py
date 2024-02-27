class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(ind, temp):
            if ind >= len(nums):
                res.append(temp[:])
                # print(temp)
                return
            
            backtracking(ind+1, temp)
            temp.append(nums[ind])
            backtracking(ind+1, temp)
            temp.pop()

        backtracking(0, [])

        return res


