class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        set_arr = set(arr)
        counts = [0] * (n + 1)
        numG = 0
        
        for num in arr:
            counts[min(num, n)] += 1
            if num > n:
                numG += 1
            
        res = n
        for i in range(n-1,-1,-1):
            if i + 1 not in set_arr:
                if numG > 0:
                    numG -= 1
                else:
                    res -= 1
            else:
                numG += counts[i+1] - 1
        return res

                
        