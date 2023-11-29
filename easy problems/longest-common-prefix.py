class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def compare(a: str, b: str)-> str:
            pointer = 0
            while(pointer < min(len(a), len(b)) and a[pointer] == b[pointer]):
                pointer +=1
            return a[:pointer]

        common = strs[0]

        for s in strs:
            common = compare(common, s)
        
        return common

        