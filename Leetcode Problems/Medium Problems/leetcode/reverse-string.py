class Solution:
    def reverseString(self, s: List[str], left = 0, right = -1) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if(right == -1):
            right = len(s)-1
        if(left > right):
            return 
        
        s[left], s[right] = s[right], s[left]

        return self.reverseString(s, left + 1, right -1)
