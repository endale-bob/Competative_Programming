class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operations = 0
        while(target != 1):
            if maxDoubles > 0 and target%2 == 0:
                target /= 2
                maxDoubles -= 1
            elif(maxDoubles == 0):
                operations += target - 1
                break
            else:
                target -= 1
            operations += 1
        
        return int(operations)