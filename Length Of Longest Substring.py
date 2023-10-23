class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        result, store = 0, defaultdict(lambda : -1)

        while(left < len(s) and right < len(s)):
            if(store[s[right]]) > -1:
                left = store[s[right]] + 1
                store.clear()
                right = left
            store[s[right]] = right
            result = max(result, right - left + 1)
            right += 1
        
        return result
