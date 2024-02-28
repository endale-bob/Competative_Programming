class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for ele in s:
            if(ele == "("):
                stack.append(0)
            else:
                temp = stack.pop()
                if(temp == 0):
                    stack[-1] += 1
                else:
                    stack[-1] += 2*temp
        
        return stack[-1]

                