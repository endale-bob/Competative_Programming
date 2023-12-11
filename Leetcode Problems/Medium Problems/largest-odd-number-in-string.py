class Solution:
    def largestOddNumber(self, num: str) -> str:
        pointer = len(num) - 1
        while(int(num[pointer]) % 2 == 0 and pointer >= 0):
                pointer -= 1
        
        return num[:pointer+1] 

