class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0
        ind = [0, 0]

        def computeHourglassSum(ind):
            return sum(grid[ind[0]][ind[1]: ind[1] + 3]) + grid[ind[0] +1][ind[1] +1] + sum(grid[ind[0] + 2][ind[1]: ind[1] + 3])
           
        while(ind[0] < rows-2):
            curr_sum = computeHourglassSum(ind)
            result = max(curr_sum, result)
            ind[1] += 1
            if(ind[1] >= cols -2):
                ind[1] = 0
                ind[0] += 1
            
        return result
