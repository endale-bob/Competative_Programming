class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        result = ""

        while(p1 < len(word1) and p2 < len(word2)):
            if(word1[p1:] > word2[p2:]):
                result += word1[p1]
                p1 += 1        
            else:
                result += word2[p2]
                p2 += 1
        
        result += word2[p2:] + word1[p1:]

        return result
