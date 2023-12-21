class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for ind in range(len(digits)-1, -1, -1):
            digits[ind] += 1
            digits[ind] %= 10
            if(digits[ind] > 0):
                break
        else:
            return [1] + digits
        return digits