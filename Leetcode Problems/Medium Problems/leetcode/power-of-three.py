class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(num):
            if(num == 0 or num == 3):
                return True
                
            if(num%3 != 0):
                return False
            
            return rec(num//3)
        
        if(n == 1):
            return True
        if(n == 0):
            return False
        
        return rec(n)