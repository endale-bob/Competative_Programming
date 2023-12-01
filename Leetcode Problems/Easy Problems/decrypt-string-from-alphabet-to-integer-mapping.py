class Solution:
    def freqAlphabets(self, s: str) -> str:
        left, right = 0, 2
        result = ""

        while(right < len(s)):
            if(s[right] == "#"):
                result += chr(int(s[left: right]) + 96)
                left = right + 1
                right += 3
            else: 
                result += chr(int(s[left]) + 96)
                left += 1
                right += 1
        
        while(left < len(s)):
            result += chr(int(s[left]) + 96)
            left += 1
        
        return result
