class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        left = 0

        for space in spaces:
            result += s[left:space] + " "
            left = space
        
        result += s[left:]

        return result