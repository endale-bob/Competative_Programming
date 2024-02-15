class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        res = 0
        curr = points[0]

        for ind in range(1, len(points)):
            if(points[ind][0]  <= curr[1]):
                curr = points[0] , min(curr[1], points[ind][1])
            else:
                curr = points[ind]
                res += 1
        
        return res +1

