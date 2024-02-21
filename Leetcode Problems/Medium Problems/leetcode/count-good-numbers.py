class Solution:
    def countGoodNumbers(self, n: int) -> int:
        _mod = 10**9 + 7
        def power(x, n):
            if(n == 1):
                return x
            if(n == 0):
                return 1

            temp = power(x, n // 2)

            temp *= temp
            if(n % 2 != 0):
                temp *= x
            
            temp = temp%_mod

            return temp

        if(n % 2 == 0):
                return (power(5, n // 2) * power(4, n // 2)) % _mod
        else:
            return (5 * power(5, (n-1) // 2) * power(4, (n-1) // 2)) % _mod


