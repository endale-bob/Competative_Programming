class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, math.sqrt(c)//1
        while(l <= r):
            hyp = l**2 + r**2
            if(hyp == c):
                return True
            elif(hyp < c):
                l +=1
            else:
                r -=1
        return False
