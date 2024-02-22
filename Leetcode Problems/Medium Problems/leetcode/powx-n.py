class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):
            return 1
        if(n == 1):
            return x
        if(n < 0):
            return 1/self.myPow(x, -n)

        temp = self.myPow(x, n//2) if n%2 == 0 else self.myPow(x, (n-1)//2)
        temp *= temp

        if(n%2 != 0):
            temp *= x

        return temp