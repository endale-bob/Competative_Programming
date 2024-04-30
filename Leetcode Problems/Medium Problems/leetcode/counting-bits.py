class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)

        for i in range(n+1):
            temp = i
            while temp:
                if temp & 1:
                    ans[i] += 1
                temp >>= 1
        
        return ans
