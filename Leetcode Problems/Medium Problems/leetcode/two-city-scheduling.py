class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        res = 0
        costs.sort(key = lambda x: x[0] - x[1])

        for ind in range(n):
            if(ind < n//2):
                res += costs[ind][0]
            else:
                res += costs[ind][1]

        return res