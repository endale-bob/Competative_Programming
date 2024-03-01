class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        right, left = 0, 0
        res = 0

        for ind in range(len(s)):
            seen = set()
            invalid = 0
            for j in range(ind, len(s)):
                if(s[j] not in seen):
                    if(s[j].upper() in seen or s[j].lower() in seen):
                        invalid -= 1
                    else:
                        invalid += 1
                    seen.add(s[j])

                if(invalid == 0):
                    if(j -ind + 1 > res):
                        left = ind
                        right = j+1
                        res = j -ind +1
            
        return s[left:right]
                
