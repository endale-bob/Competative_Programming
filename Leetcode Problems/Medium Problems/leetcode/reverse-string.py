class Solution:
    def reverseString(self, s: List[str], ptr = 0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if(ptr >= len(s)//2):
            return 

        s[ptr], s[-1 - ptr] = s[-1 - ptr] , s[ptr]

        return self.reverseString(s, ptr+1)
        