class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0]
        res = [0]*n

        for ind in range(n):
            temp = temperatures[ind]
            while(stack and temp > temperatures[stack[-1]]):
                curr = stack.pop()
                res[curr] = ind - curr
            
            stack.append(ind)
        
        return res

