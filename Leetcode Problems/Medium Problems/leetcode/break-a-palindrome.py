class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        left= 0

        if(n == 1): return  ''


        while(left < n//2):
            if(palindrome[left] == 'a'):
                left += 1
            else:
                return palindrome[:left] + 'a' + palindrome[left+1:]

        return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)

