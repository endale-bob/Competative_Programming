class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        winStart, winEnd = 0, 0
        store = {}

        while(winStart < len(s) > winEnd):
            if(s[winEnd] in store and store[s[winEnd]] >= winStart):
                winStart = store[s[winEnd]] + 1
            else:
                result = max(result, winEnd - winStart + 1)
                store[s[winEnd]] = winEnd
                winEnd += 1
        
        return result
                
