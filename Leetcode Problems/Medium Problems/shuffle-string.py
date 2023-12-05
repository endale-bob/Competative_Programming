class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        visited = {}
        result = [""]*len(s)
        
        for ind in range(len(s)):
            result[indices[ind]] = s[ind]

        return "".join(result)     
            