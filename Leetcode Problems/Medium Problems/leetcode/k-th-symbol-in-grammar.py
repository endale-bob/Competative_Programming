class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(n, k):
            if n == 1:
                return 0

            denom = 2**(n-1)//2
            temp = k%denom
            an = rec(n-1, temp)
            if k >= denom:
                return 1-an
            else:
                return an
        return rec(n, k-1)