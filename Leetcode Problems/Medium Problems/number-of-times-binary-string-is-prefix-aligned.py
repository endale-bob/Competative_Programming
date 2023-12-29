class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        res, curr, temp = 0,0,0
        for ind in range(len(flips)):
            curr += flips[ind]
            temp += ind+1
            if(curr == temp):
                res += 1
        
        return res


