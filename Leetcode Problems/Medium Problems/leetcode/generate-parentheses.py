class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        def backtrack(ind=0, open=0, temp = []):
            if(ind >= 2*n):
                if(open == 0):
                    result.add("".join(temp[:]))
                return

            temp.append("(")
            backtrack(ind+1, open+1, temp)
            temp.pop()
            
            if(open > 0):
                temp.append(")")
                backtrack(ind+1, open-1, temp)
                temp.pop()
        
        backtrack()
        return result