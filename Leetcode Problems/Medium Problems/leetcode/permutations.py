class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(temp=set(), lst=[]):
            if(len(temp) == len(nums)):
                res.append(lst[:])
                return 

            for num in nums:
                if(num in temp): continue
                lst.append(num)
                temp.add(num)
                backtracking(temp, lst)
                lst.pop()
                temp.remove(num)

        
        backtracking()
        return res