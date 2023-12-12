class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while(True):
            if(n in seen):
                return False
            else:
                seen.add(n)
                n = sum([int(num)**2 for num in str(n)])
                if(n == 1):
                    return True
                