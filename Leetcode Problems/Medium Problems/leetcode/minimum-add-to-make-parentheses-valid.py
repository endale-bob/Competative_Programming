class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        add = 0
        for ele in s:
            if(ele == "("):
                stack.append(ele)
            else:
                if(len(stack) > 0):
                    stack.pop()
                else:
                    add += 1
        add += len(stack)
        return add