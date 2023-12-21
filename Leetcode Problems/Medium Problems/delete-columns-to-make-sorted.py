class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        last = ''

        for col in range(len(strs[0])):
            last = strs[0][col]
            for row in range(1, len(strs)):
                if(strs[row][col] < last):
                    result += 1
                    break
                last = strs[row][col]

        
        return result