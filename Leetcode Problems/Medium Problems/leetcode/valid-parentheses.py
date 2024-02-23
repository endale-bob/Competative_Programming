class Solution:
    def isValid(self, s: str) -> bool:
        valid = []

        close = {
            ')' :'(',
            '}': '{',
            ']': '[',
        }

        
        for i in s:
            if(i == '(' or i == '{' or i == '[' ):
                valid.append(i)
            else:
                if(len(valid) ==0): return False
                if(valid[-1] != close[i]):
                    return False
                else: valid.pop()
        return True if len(valid) == 0  else False