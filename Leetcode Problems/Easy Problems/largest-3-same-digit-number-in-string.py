class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""

        for ind in range(2, len(num)):
            temp = num[ind - 2: ind+1]
            if(temp[0]*3 == temp and temp > result): 
                result = temp
        
        return result