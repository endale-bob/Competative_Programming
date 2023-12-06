class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        counter = 0
        result = 0
#  1%7 = 1
        for ind in range(n):
            result += (ind%7) + start
            counter += 1
            if(counter == 7):
                start += 1
                counter = 0
        
        return result



