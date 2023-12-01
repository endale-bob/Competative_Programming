class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        pointer = 0
        minLen = min(len(word1), len(word2))
        while (pointer < minLen):
            result += word1[pointer]
            result += word2[pointer]
            pointer += 1
        result += word1[pointer: len(word1)]
        result += word2[pointer: len(word2)]

        return result


        