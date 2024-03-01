class Solution:
    def letterCombinations(self, n: str) -> List[str]:
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(ind, temp):
            if(ind >= len(n)):
                curr = "".join(temp)
                if(curr): res.append(curr)
                return
            
            for ele in options[int(n[ind])]:
                temp.append(ele)
                backtrack(ind+1, temp)
                temp.pop()
        
        backtrack(0, [])
        return res
