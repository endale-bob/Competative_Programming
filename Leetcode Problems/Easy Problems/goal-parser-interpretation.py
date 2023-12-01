class Solution:
    def interpret(self, command: str) -> str:
        left, right = 0,1
        result = []
        while(right <= len(command)):
            temp = command[left: right]
            if(temp == "G" or temp == "()" or temp == "(al)" ):
                if(temp != "G"): temp = "o" if temp == "()" else "al"
                result.append(temp)
                left = right
            right += 1
        
        return "".join(result)
            
        