class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def rec(num):
            if(num == 0 or num == 4):
                return True
                
            if(num%4 != 0):
                return False
            
            return rec(num//4)
        
        if(n == 1):
            return True
        if(n == 0):
            return False
        
        return rec(n)