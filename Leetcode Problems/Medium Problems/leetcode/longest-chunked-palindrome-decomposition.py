class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        count = 0
        start = 0
        length = len(text)
        
        for end in range(length//2):            
            hasMatch = True
            
            for indx in range(start, end + 1):
                if text[indx] != text[length - (end + start) + indx - 1]:
                    hasMatch = False
                    break                
            
            if hasMatch:
                count += 2
                start = end + 1
        
        if start < (length + 1)//2:
            count += 1
            
        return count
